dict = {}

dict['M'] = 'a'
dict['T'] = 'n'
dict['N'] = 'd'
dict['J'] = 't'
dict['P'] = 'h'
dict['X'] = 'e'
dict['B'] = 'i'
dict['R'] = 's'
dict['L'] = 'm'
dict['W'] = 'g'
dict['H'] = 'k'
dict['Y'] = 'w'
dict['C'] = 'o'
dict['I'] = 'f'
dict['V'] = 'r'
dict['D'] = 'v'
dict['G'] = 'l'
dict['Q'] = 'p'
dict['F'] = 'b'
dict['A'] = 'c'
dict['S'] = 'p'
dict['E'] = 'y'
dict['U'] = 'u'
dict['K'] = 'q'
dict['Z'] = 'x'
dict['O'] = 'z'

file = open('Stage1/encrypted.txt', encoding='utf8')
message = file.read()
file.close

file = open('Stage1/decrypted.txt', 'w', encoding = 'utf8')

for char in message:
    if char in dict.keys(): file.write(dict[char])
    else: file.write(char)
