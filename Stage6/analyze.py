from util import *

file = open('Stage6/encrypted.txt')
encrypted = file.read().replace('\n', '')
file.close()

outputFile = 'Stage6/analysis.txt'

generateSnippets("the", encrypted, outputFile, snippets=200)