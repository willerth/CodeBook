import os

KEYWORD_LENGTH = 5

file = open('Stage4/encrypted.txt')
code = file.read().replace(' ', '').replace('\n', '')

directory = 'Stage4/subciphers'

if not os.path.exists(directory): os.mkdir(directory)

for i in range(KEYWORD_LENGTH):
    file = open(f'{directory}/subcipher{i}', 'w')
    j = 0
    while i + j < len(code):
        file.write(code[i + j])
        j += KEYWORD_LENGTH
        if not j % 210 : file.write('\n')

    file.close()