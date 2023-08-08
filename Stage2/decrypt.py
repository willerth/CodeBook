count = {}
file = open('Stage2/encrypted.txt', encoding='utf8')
message = file.read()
file.close

file = open('Stage2/decrypted.txt', 'w', encoding = 'utf8')

for i in range(1, 26):
    file.write(f'{i}\n')
    for char in message:
        if not char.isalpha():
            file.write(char)
            continue
        plainCharVal = ord('A') + (ord(char) - ord('A') + i) % 26
        file.write(chr(plainCharVal))

    file.write('\n\n')

    

