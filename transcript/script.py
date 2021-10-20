from typing import Dict, List
import json
import operator

PATH_CLEANED_WORDS = "D:\\german-speechdata-package-v2.tar\\german-speechdata-package-v2\\SentencesAndIDs.cleaned.txt"
PATH_ARBEITSBUCH_B2 = "D:\\Materiały\\Sicher_B2\\AB_txt_transkript.txt"
PATH_KURSBUCH_B2 = "D:\Materiały\Sicher_B2\KB_txt_transkript.txt"
PATH_ARBEITSBUCH_C1 = "D:\Materiały\Sicher_C1\AB_txt_transkript.txt"
PATH_KURSBUCH_C1 = "D:\Materiały\Sicher_C1\KB_txt_transkript.txt"
PATH_KURSBUCH_B1 = "D:\Materiały\Sicher_B1\KB_txt_transkript.txt"


PATH_LIST = [PATH_ARBEITSBUCH_B2, PATH_CLEANED_WORDS, PATH_KURSBUCH_B2, PATH_ARBEITSBUCH_C1, PATH_KURSBUCH_C1, PATH_KURSBUCH_B1]

def read_lines(path_to_file: str) -> List[str]:
    with open(path_to_file, encoding="utf-8") as file:
        lines = file.readlines()
    return lines

def split_by_words(lines: List[str]) -> List[str]:
    words = []
    tmp = []
    for line in lines:
        tmp.clear()
        tmp = line.split(' ')
        for word in tmp:
            if word.isdigit():
                continue
            else:
                words.append(word)
    return words

def count_words(words: List[str]) -> Dict:
    occurence = {}
    for word in words:
        lowercase_word = word.lower()
        if not occurence.get(lowercase_word):
            occurence[lowercase_word] = 1
        else:
            occurence[lowercase_word] = occurence[lowercase_word] + 1
    return occurence

def clean_words(words: List[str]):
    for counter, word in enumerate(words):
        words[counter] = str(word).strip('\n\t\.\,\:\"\„\-\!\?\—\""')

def count_all_world(dictionary: Dict, dict_all_words: Dict) -> Dict:
    for key in dictionary.keys():
        if not dict_all_words.get(key):
            dict_all_words[key] = dictionary[key]
        else:
            dict_all_words[key] += dictionary[key]

    return dict_all_words

def save_to_JSON(words_counter: Dict, filename: str):
    with open(f"{filename}.json", 'w', encoding='utf-8') as file:
        json.dump(words_counter, file, ensure_ascii=False)

def main():
    dict_words = {}
    dict_all_words = {}
    
    for counter, path in enumerate(PATH_LIST):
        words = read_lines(path_to_file=path)
        splitted_words = split_by_words(lines=words)
        clean_words(words=splitted_words)
        dict_words = count_words(words=splitted_words)
        save_to_JSON(words_counter=dict_words, filename=f"words_{counter}")
        all_dictionary = count_all_world(dictionary=dict_words, dict_all_words=dict_all_words)
    
    sorted_all_dict = dict(sorted(all_dictionary.items(), key=operator.itemgetter(1), reverse=True))
    save_to_JSON(words_counter=sorted_all_dict, filename="all")

if __name__ == "__main__":
    main()