import re
import pprint
import json

# file open
f = open("shrek.txt", 'r')
data = f.read()
f.close()

# split scene text
head = re.compile("^[IE][A-Z.' -]+", re.MULTILINE)
heads = head.split(data)
heads_ = head.findall(data)

# count scene
heads_length = len(heads)

# json
json_data = {}

i = 0
for head_ in heads:
    # scene json
    sh_json = {}
    # prolog content pass
    if i == 0:
        i += 1
        continue

    # author find
    a = re.compile("^ {20,24}[A-Z '0-9]+", re.MULTILINE)
    if (i < heads_length):
        # scene name
        print(i, [i - 1])
        sh_json["Heading"] = heads_[i - 1]
        i += 1

    Names = {}
    Names_ = a.findall(head_)
    # author count
    for Name in Names_:
        aa = re.compile("[A-Z0-9][A-Z' 0-9]+")
        CName = aa.search(Name)
        CN = CName.group()
        if CN in Names.keys():
            Names[CN] = Names.get(CN) + 1
        else:
            Names[CN] = 1
    # author count put json
    sh_json["Characters"] = Names

    # scene data put main json
    json_data["SH"+str(i-1)] = sh_json
    # author print
    for CN in Names:
        print(Names[CN], "\t", CN)
    print("\n")

# json save
with open("shrek.json", "w", encoding="utf-8") as make_json:
    json.dump(json_data, make_json, indent="\t")
pprint.pprint(json_data)
