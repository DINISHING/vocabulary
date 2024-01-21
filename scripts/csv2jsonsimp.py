#! python3

'''
用於將 characters.csv 轉換成適合前端標音用个 json

輸出格式
{ "字": [音1, 音2]}
'''

import csv
import json

res = {}

with open("characters.csv", "r", encoding="utf-8") as f:
    charlist = csv.reader(f,  delimiter=',')
    for item in list(charlist)[1:]:
        char, phon = item[0:2]
        if (phon):
            if char not in res:
                res[char] = []
            res[char].append(phon)

with open("build/char_phon_simp.json", "w", encoding="utf-8") as f:
    json.dump(res, f)
