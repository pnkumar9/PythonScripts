'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
'''

def detectCapital1(word):
    #count number of caps and small in the word
    caps = 0
    small = 0

    for ch in word:
        if 'A' <= ch <= 'Z':
            caps += 1
        if 'a' <= ch <= 'z':
            small += 1

    return caps == len(word) or small == len(word) or (caps == 1 and  'A' <= word[0] <= 'Z')

print(detectCapital1("USA"))     
print(detectCapital1("Faang"))     
print(detectCapital1("leetcode"))  
print(detectCapital1("FaanG"))    

def detectCapital2(word):
    return all('A' <= ch <= 'Z' for ch in word) or \
           all('a' <= ch <= 'z' for ch in word) or \
           ('A' <= word[0] <= 'Z' and all('a' <= ch <= 'z' for ch in word[1:]))

print(detectCapital2("USA"))     
print(detectCapital2("Faang"))     
print(detectCapital2("leetcode"))  
print(detectCapital2("FaanG"))           