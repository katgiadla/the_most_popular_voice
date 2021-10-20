from io import DEFAULT_BUFFER_SIZE
from typing import List
from pydub import AudioSegment
from pydub.silence import split_on_silence
from os.path import join
import os

DESTINATION_PATH = "D:\\master_thesis_records\\records\\splits\\wir"
RECORDS_PATH = "D:\\master_thesis_records\\records\\to_split\\wir"

def split_audio_record(path: str):
    speed = 0.95

    if path.endswith("wav"):
        sound = AudioSegment.from_wav(path)
    elif path.endswith("mp3"):
        sound = AudioSegment.from_mp3(path)
    else:
        pass

    max_volume = sound + 12
    max_volume_slowed = max_volume._spawn(max_volume.raw_data, overrides= {
        "frame_rate": int(max_volume.frame_rate * speed)
    })

    slices = split_on_silence(max_volume_slowed.set_frame_rate(max_volume.frame_rate), min_silence_len=125, silence_thresh=-16)
    return slices

def save_slices_to_wave(slices: List, filename: str) -> None:
    output_path = join(DESTINATION_PATH, f"{filename}")
    os.mkdir(path=output_path)
    for counter, slice in enumerate(slices):
        result_path = join(output_path, f"word_{counter}.wav")
        slice.export(result_path, format="wav")

def main():
    for file in os.listdir(path=RECORDS_PATH):
        split_filename = join(RECORDS_PATH, file)
        splits = split_audio_record(path=split_filename)
        filename = file.split(".")[0]
        save_slices_to_wave(slices=splits, filename=filename)

if __name__=='__main__':
    main()