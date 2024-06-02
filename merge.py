from argparse import ArgumentParser
from pathlib import Path
from pydub import AudioSegment
from tqdm import tqdm


def mapping_merge_wav(input_dir, mapping_list_path, output_dir):
    with mapping_list_path.open('r', encoding="utf-8") as mapping_list, output_dir.joinpath("merged_mapping.list").open("w", encoding="utf-8") as new_mapping_list:
        lines = list(mapping_list)
        counter = 1
        texts_buffer = []
        audio_paths_buffer = []

        print(f"\n{mapping_list_path}")
        for line in tqdm(lines, desc="合并中"):
            audio_path = input_dir / line.split("|")[0]
            text = line.split('|')[1].replace('\n', '')
            if any(char in {'。', '.'} for char in (text[-2::])) or not line:
                new_audio_name = f"{counter}.wav"
                texts_buffer.append(text)
                merged_text = ''.join(texts_buffer)
                new_mapping_list.write(f"{new_audio_name}|{merged_text}\n")

                merged_audio = AudioSegment.empty()
                audio_paths_buffer.append(audio_path)
                for audio_segment_path in audio_paths_buffer:
                    audio_segment = AudioSegment.from_file(audio_segment_path)
                    merged_audio += audio_segment
                merged_audio.export(output_dir / new_audio_name, format="wav")

                audio_paths_buffer.clear()
                texts_buffer.clear()
                counter += 1
            else:
                texts_buffer.append(text)
                audio_paths_buffer.append(audio_path)


def main():
    parser = ArgumentParser(description="根据list映射合并wav音频")
    parser.add_argument("input", type=str, help="处理的目录")
    parser.add_argument("output", type=str, help="输出的目录")
    args = parser.parse_args()
    input_path = Path(args.input)

    for mapping_list_path in input_path.rglob("*.list"):
        input_dir = mapping_list_path.parent
        output_dir = Path(args.output) / input_dir.parts[-1]
        output_dir.mkdir(parents=True, exist_ok=True)

        mapping_merge_wav(input_dir, mapping_list_path, output_dir)


if __name__ == "__main__":
    main()
