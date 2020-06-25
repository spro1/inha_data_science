import re

# file open
f = open("shrek.txt", 'r')
data = f.readlines()
f.close()

# search header pattern
p = re.compile("^[IE][A-Z.' -]+", re.MULTILINE)
# search author pattern
p2 = re.compile("^ {20,25}[A-Z 0-9(O.S.)]+", re.MULTILINE)
result = {}
header = None
for i in data:
    head = p.findall(i)
    author = p2.findall(i)
    if not head:
        pass
    else:
        header = head[0]
        if result:
            for key, value in result.items():
                print("%s\t%s" % (value, key))
            print("\n")
            result = {}
        print(header)
    if author and header:
        author = author[0].lstrip(" ")
        if author in result.keys():
            result[author] = result.get(author) + 1
        else:
            result[author] = 1

for key, value in result.items():
    print("%s\t%s" % (value, key))

"""output
INT. INSIDE CHURCH
18	SHREK
14	FIONA
12	FARQUAAD
4	DONKEY
1	CONGREGATION
1	WHISPERS


EXT. THE SWAMP
1	GINGERBREAD MAN
1	DONKEY
"""