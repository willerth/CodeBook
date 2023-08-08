file = open('Stage3/encrypted.txt')
code = file.read()
file.close()

chars = {}
doubleLetters = {}

for i in range(len(code) - 1):
    firstChar = code[i]
    secondChar = code[i + 1]

    if firstChar == secondChar:
        if not firstChar in doubleLetters: doubleLetters[firstChar] = 0
        doubleLetters[firstChar] += 1

    if(firstChar not in chars.keys()):
        chars[firstChar] = {'occurrences': 0}
    chars[firstChar]['occurrences'] += 1

    if(secondChar not in chars[firstChar].keys()):
        chars[firstChar][secondChar] = 0
    
    chars[firstChar][secondChar] += 1

file = open("Stage3/util.txt", "w")

for char in dict(sorted(chars.items())):
    if(char == '\n'): continue
    file.write(f"{char} ({chars[char]['occurrences']})\n")
    for following in chars[char].keys():
        if(following in ['\n', 'occurrences']): continue
        file.write(f'{following} : {chars[char][following]}\n')
    file.write('\n')

file.write('\n\nDOUBLE LETTERS:\n')
for letter in doubleLetters: file.write(f'{letter} : {doubleLetters[letter]}\n')

file.close()