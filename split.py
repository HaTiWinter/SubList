from argparse import ArgumentParser
from pathlib import Path
from pydub import AudioSegment
from tqdm import tqdm


def unformat(timestamp):
    h, m, s, ms = map(int, (timestamp[:2], timestamp[3:5], timestamp[6:8], timestamp[9:]))

    return h * 3600000 + m * 60000 + s * 1000 + ms


def srt_split_wav(subtitle_path, audio_path, output_dir):
    with subtitle_path.open('r', encoding="utf-8") as subtitle, output_dir.joinpath("splitted_mapping.list").open('w', encoding="utf-8") as mapping_list:
        subtitle_data = subtitle.read().split("\n\n")
        audio_segment = AudioSegment.from_file(audio_path)

        print(f"\n{subtitle_path}")
        for block in tqdm(range(len(subtitle_data) - 1), desc="切分中"):
            lines = subtitle_data[block].split('\n')
            audio_name = f"{lines[0]}.wav"
            text = '\n'.join(lines[2:])
            mapping_list.write(f"{audio_name}|{text}\n")

            start_time, end_time = [unformat(timestamp) for timestamp in lines[1].split(" --> ")]
            audio_segment[start_time:end_time].export(output_dir / audio_name, format="wav")


def main():
    parser = ArgumentParser(description="根据srt字幕切分wav音频")
    parser.add_argument("input", type=str, help="处理的目录")
    parser.add_argument("output", type=str, help="输出的目录")
    args = parser.parse_args()

    for subtitle_path in Path(args.input).rglob("*.srt"):
        output_dir = Path(args.output) / subtitle_path.stem
        output_dir.mkdir(parents=True, exist_ok=True)
        audio_path = subtitle_path.with_suffix(".wav")

        srt_split_wav(subtitle_path, audio_path, output_dir)


if __name__ == "__main__":
    main()
