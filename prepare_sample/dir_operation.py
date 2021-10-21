import os.path
import os
import typing
import scipy.io.wavfile
import numpy as np

def load_dir(dir_path: str) -> typing.List[str]:
    return os.listdir(dir_path) if os.path.isdir(dir_path) else None

def open_wav_file(path: str):
    rate, file = scipy.io.wavfile.read(filename=path)
    return np.array(file, dtype=float)

def get_wav_file_rate(path: str) -> int:
    rate, file = scipy.io.wavfile.read(filename=path)
    return rate