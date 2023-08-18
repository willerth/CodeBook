#Generates potential keyword snippets given an encrypted message and a common english word, and
#writes every snippet to a given output file. The three optional arguments dictate how many
#snippets are generated, and at what interval
def generateSnippets(commonWord, message, filename, start=0, snippets=1000, increment=1):
    outputFile = open(filename, 'w')

    end = min(snippets, len(message) - len(commonWord) + 1)
    for i in range(start, end, increment):
        outputFile.write(f'{i}: '.rjust(5))
        for j in range(len(commonWord)):
            keyLetter = genKeyLetter(commonWord[j], message[i + j])
            outputFile.write(keyLetter)
        if i < end - 1 : outputFile.write('\n')

    outputFile.close()
        


def genKeyLetter(plainLetter, cipherLetter):
    plainPos = ord(plainLetter)
    cipherPos = ord(cipherLetter)
    difference = (cipherPos - plainPos) % 26

    keyLetter = chr(ord('A') + difference)
    return(keyLetter)