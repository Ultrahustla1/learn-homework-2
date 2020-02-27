with open('referat.txt', 'r', encoding='utf-8') as file1:
    for ln in file1:
        ln = ln.replace('.', '!')
        print(ln)

file1 = open('referat.txt', 'r', encoding='utf-8')

lines = 0
words = 0
letters = 0

for line in file1:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
print("Lines:", lines)
print("Words:", words)