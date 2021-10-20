import os
from typing import List, Dict
import numpy as np
import json
import xml.etree.ElementTree as ET

LIST_SUBDIRECTORY = ["train", "dev", "test"]
ROOT_DIRECTORY = "D:\\german-speechdata-package-v2.tar\\german-speechdata-package-v2"
LIST_WORDS = ["wir", "vier", "stadt", "staat", "zu", "zur", "wenig", "wenige", "wurden", "würden", "wurde", "würde"]

# DEBUG
# ROOT_DIRECTORY = "D:\\PythonScripts\\the_most_popular_voice"
# LIST_SUBDIRECTORY = ["dev"]

def list_xml_files(path: str) -> List[str]:
    files = os.listdir(path=path)
    for file in files:
        if not file.endswith(".xml"):
            files.remove(file)
    return files

def count_attemps(root: str, files: List[str]) -> Dict:
    ATTEMPS_DICT = {}
    
    for file in files:
        filepath = os.path.join(root, file)
        words_counter = np.zeros(12, dtype=int)
        try:
            tree = ET.parse(filepath, parser=ET.XMLParser(encoding='utf-8'))
            tree_root = tree.getroot()
            line = tree_root.find('cleaned_sentence').text
            line_lower = line.lower()
            words = line_lower.split(' ')
            for word in words:
                if word in LIST_WORDS:
                    idx = LIST_WORDS.index(word)
                    words_counter[idx] += 1
                else:
                    continue
            if np.array_equal(np.zeros(12, dtype=int), words_counter):
                continue
            else:
                print(f"{file}: {words_counter}")


                ATTEMPS_DICT[file] = words_counter
        except (Exception):
            continue
    
    return ATTEMPS_DICT

def save_to_json(output: str, attemps_dict: Dict):
    final_dict = {key:v.tolist() for key, v in attemps_dict.items()}
    with open(output, 'w') as file:
        json.dump(final_dict, file)

def main():
    for subdir in LIST_SUBDIRECTORY:
        path = os.path.join(ROOT_DIRECTORY, subdir)
        files = list_xml_files(path=path)
        records_attemps = count_attemps(root=path, files=files)
        output_path = f"./{subdir}.json"
        save_to_json(output=output_path, attemps_dict=records_attemps)
        print(records_attemps)

if __name__ == "__main__":
    main()