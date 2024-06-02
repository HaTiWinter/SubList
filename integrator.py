from argparse import ArgumentParser
from merge import mapping_merge_wav
from pack import list_pack_wav
from pathlib import Path
from shutil import rmtree
from split import srt_split_wav
from uuid import uuid4


class TempDir:
    def __init__(self, temp_path):
        self.path = temp_path

    def __enter__(self):
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        rmtree(self.path, ignore_errors=True)

def srt_pack_wav(input_path, output_path, speaker, temp_path):
    splited_path = temp_path / "splitted"
    merged_path = temp_path / "merged"

    for subtitle_path in input_path.rglob("*.srt"):
        output_dir = splited_path / subtitle_path.stem
        output_dir.mkdir(parents=True, exist_ok=True)
        audio_path = subtitle_path.with_suffix(".wav")

        srt_split_wav(subtitle_path, audio_path, output_dir)

    for mapping_list_path in splited_path.rglob("*.list"):
        input_dir = mapping_list_path.parent
        output_dir = merged_path / input_dir.parts[-1]
        output_dir.mkdir(parents=True, exist_ok=True)

        mapping_merge_wav(input_dir, mapping_list_path, output_dir)

    for mapping_list_path in merged_path.rglob("*.list"):
        output_dir = output_path / speaker
        output_dir.mkdir(parents=True, exist_ok=True)

        list_pack_wav(mapping_list_path, output_dir, speaker)


def main():
    parser = ArgumentParser(description="根据srt字幕和wav音频打包数据集")
    parser.add_argument("input", type=str, help="处理的目录")
    parser.add_argument("output", type=str, help="输出的目录")
    parser.add_argument("speaker", type=str, help="说话人")
    args = parser.parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    speaker = args.speaker

    temp_path = Path(f"{uuid4()}")
    temp_path.mkdir(parents=True, exist_ok=True)

    with TempDir(temp_path):
        srt_pack_wav(input_path, output_path, speaker, temp_path)


if __name__ == '__main__':
    main()
