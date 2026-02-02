words = list(map(str,input().split(",")))
words.sort()
short = words[0]

for word in words:
    if len(word)<len(short):
        short = word
print(short)
