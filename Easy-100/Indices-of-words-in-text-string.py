'''
Indices Of Words In Text String
Indices Of Words In Text String



Given some text and a bunch of words, find where each of the words appear in the text. Text may contain spaces, words may not.

For every given word you need to return a list of (zero-based) indices of where that word starts in the text. If a word isn’t found in the text, return [-1] for that word.



Example

Input:

text = “you are very very smart”

words = [“you”, “are”, “very”, “handsome”]



Output:

[ [0], [4], [8, 13], [-1] ]

“you” is found in the given text starting at the index 0.

“are” is found in the given text starting at the index 4.

“very” is found in the given text two times, starting at the indices 8 and 13.

“handsome” isn’t found in the given text.



Notes

Input Parameters:

Function has two arguments: string text and list of strings words.



Output: Function must return a list of lists of integers. One list for each one of the words. 
i-th list must contain all indices of characters in text where i-th word starts, in the ascending order. 
If i-th word isn’t found in the text at all, then i-th list must be [-1].
'''