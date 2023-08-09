import os

subcipherDirectory = 'Stage4/subciphers/'
startingKeys = ['S','C','U','B','A']
codes = []
messageLength = 0

for filename in os.listdir(subcipherDirectory):
    file = open(subcipherDirectory + filename)
    code = file.read().replace('\n','')
    file.close()
    codes.append(code)
    messageLength += len(code)


decryptedFile = open('Stage4/decrypted.txt', 'w')

for i in range(messageLength):
    arrIdx = i % 5
    strIdx = i // 5
    encryptedChar = codes[arrIdx][strIdx]
    alphabetPos = ord(encryptedChar) - ord(startingKeys[arrIdx])
    decryptedChar = chr(ord('A') + alphabetPos % 26)
    decryptedFile.write(decryptedChar)

decryptedFile.close()