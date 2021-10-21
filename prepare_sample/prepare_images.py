import os.path
import dir_operation
import create_images

SOURCE_DIR = "E:\\praca_magisterska\\materials\\records\\records"
# WORDS = ['würden', 'wurden', 'zu', 'zur', 'vier', 'wir', 'wenig', 'wenige', 'staat', 'stadt']

WORDS = ["staat", "stadt", 'würden', 'wurden']

RAW_IMAGES_DIR = "E:\\praca_magisterska\\materials\\images\\raw"

def prepare_images(dir_path: str):
    files = dir_operation.load_dir(dir_path)
    mfcc_engine = create_images.MFCCEngine()
    for counter, file in enumerate(files):
        input_filepath = os.path.join(dir_path, file)
        output_filepath = os.path.join(RAW_IMAGES_DIR, word)
        coeff = mfcc_engine.compute_mfcc(path=input_filepath)
        norm_coeff = mfcc_engine.normalize_mfcc(mfcc_coef=coeff)
        mfcc_engine.create_image(matrix=norm_coeff, path_to_save=output_filepath, id_sample=str(counter) + ".bmp")


if __name__ == '__main__':
    for word in WORDS:
        dir_path = os.path.join(SOURCE_DIR, word)
        prepare_images(dir_path=dir_path)