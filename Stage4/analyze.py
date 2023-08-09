import sys, os
sys.path.append(('../CodeBook'))
from frequencies import frequencies

SUBCIPHER_LENGTH = 121

directory = 'Stage4/subciphers/'

analysisFile = open('Stage4/analysis.txt', 'w')

idx = 0
for filename in os.listdir(directory):
    file = open(directory + filename)
    code = file.read()
    file.close

    for char in code:
        if char == '\n': continue
        frequencies[char] += 1

    analysisFile.write(f'SUBCIPHER {idx}\n')
    for key in frequencies.keys():
        frequency = '{0:.2f}'.format(frequencies[key] / SUBCIPHER_LENGTH * 100)
        analysisFile.write(f'{key} : {frequency}\n')

    

    analysisFile.write('\n\n')
    idx += 1

    for key in frequencies.keys() : frequencies[key] = 0

