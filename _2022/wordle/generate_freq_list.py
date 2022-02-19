import json
import unicodedata
import numpy as np
import os


def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])


# os.chdir('D:\\Documents\\Programmation\\Python\\videos\\_2022\\wordle')
LEXICON = "D:\\Downloads\\Lexique383\\Lexique383.tsv"
word_list = []
d = dict()
with open('data/possible_words_en.txt') as f:
    word_list = [s.strip() for s in f.readlines()]

word_list.sort()

with open(lexique, 'r', encoding='utf-8') as f:
    for lines in f.readlines()[1:]:
        line_split = lines.split('\t')
        if int(line_split[14]) == 5:
            word = remove_accents(line_split[0])
            freq = [float(s) for s in line_split[8:9]]
            if word in word_list and word not in d.keys():
                d[word] = np.mean(freq)/1e6

word_missing = [w for w in word_list if w not in d.keys()]
for w in word_missing:
    d[w] = 1e-12

with open('data/freq_map_fr.json','w') as f:
    json.dump(d,f)
