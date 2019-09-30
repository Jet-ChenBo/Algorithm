#统计文本中单词出现的频率
def getText():
    txt = open("C:/Users/Administrator/Desktop/hello.txt", "r").read()
    txt = txt.lower()
    for ch in ',.':
        txt = txt.replace(ch, " ")
    return txt

cbTxt = getText()
words = cbTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
print(items)
#items.sort(key=lambda x:x[1],reverse=True)
for i in range(8):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
