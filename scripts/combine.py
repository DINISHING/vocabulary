#! python3

chars = []


def readlist(filename):
    with open(filename, "r", encoding="utf-8") as f:
        charlist = f.readlines()
        for item in list(charlist)[1:]:
            if item[0] == "#":
                continue
            chars.append("\t".join(item.rstrip().split("\t")[0:3]))

readlist("chars-supp.tsv")
readlist("chars-main.tsv")

with open("chars-combined.tsv", "w", encoding="utf-8") as f:
    f.write("\n".join(chars))
