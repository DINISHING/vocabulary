# 標準吳語詞庫

該許記錄標準吳語个讀音，詞彙。目標是可以作爲標吳詞典與標吳輸入法詞庫。

正體用詞請按照 OpenCC 標準。

初始來源 <https://github.com/saeziae/rime_nguphing>，以後將以此倉庫爲輸入法字音與詞彙來源。

文件結構：

- `chars-main.tsv` 根據中古推導个字音表。請保持原順序，覅个字請打`#`來忽略。
- `chars-supp.tsv` 弗符合中古个發音
- `common-words.tsv` 推導个詞彙表，用于多音字問題
- `words.tsv` 吳語詞彙
- `no-words.tsv` 弗適合作爲詞典詞彙，但是適合加入輸入法。一方面是組合用法如「我个」，多音字組詞如「睏覺」。
- `maps.tsv` 吳越地名
- `phrases.tsv` 熟語

老文件：

- `characters.csv` 單字音
- `words-legacy.tsv` 原輸入法个詞彙庫

表頭：

- 字：openCC 正體中文
- 權重，百分比，低於 5%弗參加組詞
- 音類
  - 慣：慣用音
  - 口：口語音，一般與韻書音協同使用
  - 韻：韻書音
  - 訓：訓讀音
  - 漢：漢音，文讀音
  - 古：滯古音
- 釋義：用「；」分割，用「【】」組詞搭引用，用『「」』組句

## 在線 json 引用

<https://dinishing.github.io/vocabulary/char_phon_simp.json>
