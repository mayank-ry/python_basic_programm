words = list(map(str,input().split(",")))

length_word = []
total = 0
count = 0

for word in words:
    length_word.append(len(word))

for num in length_word:
    total += num

avg = total / len(words)

avg = int(avg) if avg == int(avg) else int(avg) + 1
for word in words:
    if len(word) > avg:
        count += 1

print(count)
