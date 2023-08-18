def generateSnippets(commonWord, message, outputFile):
    for i in range(len(message) - len(commonWord) + 1):
        for j in range(len(commonWord)):
            keyLetter = genKeyLetter(commonWord[j], message[i + j])
            outputFile.write(keyLetter)
        if(i < len(message) - len(commonWord)): outputFile.write('\n')
        


def genKeyLetter(plainLetter, cipherLetter):
    plainPos = ord(plainLetter)
    cipherPos = ord(cipherLetter)
    difference = (cipherPos - plainPos) % 26

    keyLetter = chr(ord('A') + difference)
    return(keyLetter)