#!/usr/bin/env python3.6

'''
Sentence Reversal¶
Problem
Given a string of words, reverse all the words. For example:
Given:

'This is the best'

Return:
'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
'  space here'  and 'space here 

'''
def rev_word1(s):
    return " ".join(reversed(s.split()))

#Or

def rev_word2(s):
    return " ".join(s.split()[::-1])


def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """
    
    words = []
    length = len(s)
    spaces = [' ']
    
    # Index Tracker
    i = 0
    
    # While index is less than length of string
    while i < length:
        
        # If element isn't a space
        if s[i] not in spaces:
            
            # The word starts at this index
            word_start = i
            
            while i < length and s[i] not in spaces:
                
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1
        
    # Join the reversed words
    return " ".join(reversed(words))

print(rev_word1('Hi John,   are you ready to go?'))
print(rev_word2('Hi John,   are you ready to go?'))
print(rev_word3('Hi John,   are you ready to go?'))    