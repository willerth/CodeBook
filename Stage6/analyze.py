from util import *

file = open('Stage6/encrypted.txt')
encrypted = file.read().replace('\n', '')
file.close()

outputFile = open('Stage6/analysis.txt','w')

generateSnippets("the", encrypted, outputFile)

outputFile.close()