def maximumOccurringCharacter(text):
    # Write your code here
    charFreq = dict()
    maxFreq = 0
    
    for ch in text:
        if ch in charFreq:
            charFreq[ch] += 1
            if charFreq[ch] > maxFreq:
                maxFreq = charFreq[ch]
        else:
            charFreq[ch] = 1
            
    for ch in text:
        if charFreq[ch] == maxFreq:
            return ch
            


print(maximumOccurringCharacter('hellowrld'))
print(maximumOccurringCharacter('aabccdee'))