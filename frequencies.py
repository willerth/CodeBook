#create empty dictionary of frequencies - initialize each frequency to zero
frequencies = {}

for i in range(26):
    frequencies[chr(ord('A') + i)] = 0