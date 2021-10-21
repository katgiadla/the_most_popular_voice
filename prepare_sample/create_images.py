from speechpy.feature import mfcc
from numpy import array, min, ptp
from PIL import Image, ImageOps, ImageFilter
from os.path import join
import dir_operation

class MFCCEngine:
    def __init__(self):
        self.no_of_melfilters = 26
        self.no_of_cepstrum = self.no_of_melfilters+2
        self.fft_size = 1024
        self.low_freq = 20.0
        self.max_freq = 8000.0
        self.HIGH = 56
        self.WIDTH = self.no_of_melfilters

    def compute_mfcc(self, path: str) -> array:
        wav_file = dir_operation.open_wav_file(path)
        mfcc_coef =  mfcc(wav_file, dir_operation.get_wav_file_rate(path), frame_length=0.024, num_cepstral=self.no_of_cepstrum,
                    num_filters=self.no_of_melfilters, fft_length=self.fft_size, low_frequency=self.low_freq,
                    high_frequency=self.max_freq)
        return mfcc_coef

    def normalize_mfcc(self, mfcc_coef: array) -> array:
        normalized_coeff = (255 * (mfcc_coef - min(mfcc_coef))/ptp(mfcc_coef)).astype(int)
        return normalized_coeff

    def create_image(self, matrix: array, path_to_save: str, id_sample: str):
        img = Image.fromarray(matrix)
        gray_image = ImageOps.grayscale(img)
        gray_image.filter(ImageFilter.GaussianBlur)
        gray_image = gray_image.resize((self.WIDTH, self.HIGH), Image.ANTIALIAS)
        gray_image.save(join(path_to_save, id_sample))