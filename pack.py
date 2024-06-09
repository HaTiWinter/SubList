from argparse import ArgumentParser
from pathlib import Path
from py3langid.langid import classify, set_languages
from pydub import AudioSegment
from tqdm import tqdm
from uuid import uuid4

set_languages(langs=["zh", "en"])


def list_pack_wav(mapping_list_path, output_dir, speaker):
    new_mapping_list_path = output_dir / "packed_mapping.list"

    with mapping_list_path.open('r', encoding="utf-8") as mapping_list, new_mapping_list_path.open('a', encoding="utf-8") as new_mapping_list:
        lines = list(mapping_list)

        print(f"\n{mapping_list_path}")
        for line in tqdm(lines, desc="打包中"):
            text = line.split('|')[1]
            language = classify(text)[0].upper()
            new_audio_file_name = f"{speaker}_{uuid4()}.wav"
            new_mapping_list.write(f"./{output_dir.parts[-2]}/{output_dir.parts[-1]}/{new_audio_file_name}|{speaker}|{language}|{text}")

            audio_path = line.split('|')[0]
            source_audio_path = mapping_list_path.parent / audio_path
            dest_audio_path = output_dir / new_audio_file_name
            audio_segment = AudioSegment.from_file(source_audio_path)
            audio_segment.export(dest_audio_path, format="wav")


def main():
    parser = ArgumentParser(description="根据list映射和wav音频打包数据集")
    parser.add_argument("input", type=str, help="处理的目录")
    parser.add_argument("output", type=str, help="输出的目录")
    parser.add_argument("speaker", type=str, help="说话人")
    args = parser.parse_args()
    speaker = args.speaker

    for mapping_list_path in Path(args.input).rglob("*.list"):
        output_dir = Path(args.output) / speaker
        output_dir.mkdir(parents=True, exist_ok=True)

        list_pack_wav(mapping_list_path, output_dir, speaker)


if __name__ == "__main__":
    main()
