import re

# file open
f = open("shrek.txt", 'r')
data = f.read()
f.close()

'''
#scene heading split
headers = re.split("(INT.)|(EXT.)", data)
print((headers)
'''


# search header pattern
p = re.compile("^[IE][A-Z.' -]+", re.MULTILINE)
# search author pattern
p2 = re.compile("^ {20,25}[A-Z 0-9(O.S.)]+", re.MULTILINE)

# scripts : text split
scripts = []
# header values
headers = p.findall(data)
# text split
for i in headers:
    split_text = re.split(i, data)
    scripts.append(split_text[0])
    # 중복 header 값 split data join
    split_text = i.join(split_text[1:])
    data = split_text
scripts.append(data)

# load split text, search author
for idx, val in enumerate(scripts):
    if idx != 0:
        # result : author counting dict
        result = {}
        # print Scene heading
        print(headers[idx-1])
        authors = p2.findall(val)
        for author in authors:
            # 왼쪽 공백 제거
            author = author.lstrip(" ")
            # 카운팅
            if author in result.keys():
                result[author] = result.get(author) + 1
            else:
                result[author] = 1
        # 카운팅 값 기준으로 내림차순 정렬
        # dict -> list[tuple]
        result = sorted(result.items(), key=lambda x: x[1], reverse=True)
        # print author count
        for i in result:
            print("%s\t%s" % (i[1], i[0]))
        print("\n")


'''
output example
    (...)
    INT. FIONA'S ROOM
    32	FIONA
    31	SHREK
    7	DONKEY
    1	DONKEY(O.S.)


    EXT. WOODS
    5	FIONA
    4	DONKEY
    4	SHREK
    (...)
'''