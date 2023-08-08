MAX_SEARCH_LENGTH = 7
MIN_SEARCH_LENGTH = 4

#just define the first three ordinal numbers - these will be used in util.txt to
#describe occurences of the same substring in the ciphertext. It's hard coded write
#now, which kinda sucks, but no pattern appears more than three times. It works.
ordinals = ['first', 'second', 'third']

file = open('Stage4/encrypted.txt')
#We're getting rid of whitespace here because it complicates the analysis

code = file.read().replace(' ', '').replace('\n','')
file.close()
totalPatterns = {}

file = open('Stage4/util.txt', 'w')
for SEARCH_LENGTH in range(MAX_SEARCH_LENGTH, MIN_SEARCH_LENGTH - 1, -1):
    #totalPatterns stores every pattern found multiple times
    #patterns stores every substring of a length SEARCH_LENGTH. Substrings that appear only once get removed,
    #and remaining substrings are checked to see if they're substrings of patterns that have already been found.
    #This is the motivation for going backwards through this outer loop - we want to first find the longest
    #patterns, and then find shorter patterns that haven't already been found. See notes.txt
    #Each pattern maps to an array, the first element of which tracks the number of occurences, and whose
    #other elements track the position of the pattern in the ciphertext
    patterns = {}
    for i in range(len(code) - SEARCH_LENGTH + 1):
        j = 0
        stringBuilder = ""
        while len(stringBuilder) < SEARCH_LENGTH and i + j < len(code):
            stringBuilder += code[i + j]
            j += 1
        if(not stringBuilder in patterns.keys()): patterns[stringBuilder] = [0]
        patterns[stringBuilder][0] += 1
        patterns[stringBuilder].append(i)

    #get rid of patterns that aren't really patterns
    for pattern in list(patterns):
        if(patterns[pattern][0] == 1):
            del patterns[pattern]
            continue

    #get rid of patterns that have already been stored in totalPatterns
        patternExists = False
        for longerPattern in totalPatterns:
            if pattern in longerPattern:
                patternExists = True
        
        if not patternExists:
            totalPatterns[pattern] = patterns[pattern]


#Document each pattern in util.txt
for pattern in totalPatterns:
    arr = totalPatterns[pattern]
    occurrences = arr[0]
    file.write(f'{pattern} occurs {occurrences} times, with positions:\n')
    for i in range(1, len(arr)):
        file.write(f'\t{arr[i]}\n')
    for i in range(2, len(arr)):
        first = arr[i-1]
        last = arr[i]

        firstOrdinal = ordinals[i - 2]
        secondOrdinal = ordinals[i - 1]
        file.write(f'There are {last - first} characters between the start of the {firstOrdinal} and {secondOrdinal} occurrence.\n')
    file.write('\n------\n\n')

file.close()