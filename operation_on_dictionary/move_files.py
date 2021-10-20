import os
import shutil
import re

FILE_LIST_DEV = ["2015-01-28-14-05-03.xml",
"2015-02-09-13-37-16.xml",
"2015-01-28-11-43-18.xml",
"2015-01-28-13-58-36.xml",
"2015-02-09-12-32-04.xml",
"2015-02-09-12-36-27.xml",
"2015-02-09-13-33-38.xml"
]

FILE_LIST_TEST = ["2015-01-28-11-51-16.xml",
"2015-02-04-14-17-26.xml",
"2015-01-27-12-43-24.xml",
"2015-01-27-13-41-57.xml",
"2015-01-28-11-51-53.xml",
"2015-02-04-14-09-15.xml",
"2015-02-09-12-13-40.xml",
"2015-02-10-11-38-07.xml",
"2015-02-10-11-41-21.xml",
"2015-02-10-13-43-54.xml"
]

FILE_LIST_TRAIN = ["2014-03-17-13-20-25.xml",
"2014-03-17-14-37-39.xml",
"2014-03-17-14-45-12.xml",
"2014-03-17-15-12-53.xml",
"2014-03-18-11-06-06.xml",
"2014-03-19-13-12-11.xml",
"2014-03-19-13-09-23.xml",
"2014-03-19-13-11-32.xml"
]

FILE_LISTS = [FILE_LIST_DEV, FILE_LIST_TEST, FILE_LIST_TRAIN]
# FILE_LISTS = [FILE_LIST_DEV, FILE_LIST_TEST]
SOURCE_PATH = "D:\\german-speechdata-package-v2.tar\\german-speechdata-package-v2\\"
SUBDIRECTORIES = ["dev", "test", "train"]
# SUBDIRECTORIES = ["dev", "test"]

OUTPUT_DIR = "D:\\master_thesis_records\\records\\to_split\\vier"

def check_pattern(counter: int, filename: str) -> bool:
    result = False
    if filename.endswith("Realtek.wav"):
        result = False
    else:
        for pattern in FILE_LISTS[counter]:
            compiled_pattern = re.compile(pattern)
            if compiled_pattern.match(filename):
                result = True
            else:
                continue
    return result

def main():
    for counter, subdir in enumerate(SUBDIRECTORIES):
        source = os.path.join(SOURCE_PATH, subdir)
        file_list = os.listdir(path=source)
        for file in file_list:
            if file.endswith(".xml"):
                if check_pattern(counter=counter, filename=file):
                    shutil.copy2(os.path.join(source, file), OUTPUT_DIR)

if __name__ == '__main__':
    main()