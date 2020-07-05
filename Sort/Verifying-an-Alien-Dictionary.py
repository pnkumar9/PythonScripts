#!/usr/bin/env python3.6

'''
Given a sequence of Words and the Order of the alphabet. 
The order of the alphabet is some permutation of lowercase letters. 
The task is to check whether the given words are sorted lexicographically according to order of alphabets.
 Return “True” if it is, otherwise “False”.

Input : Words = [“hello”, “leetcode”], Order = “habcldefgijkmnopqrstuvwxyz”
Output : true

Input : Words = [“word”, “world”, “row”], Order = “abcworldefghijkmnpqstuvxyz”
Output : false
Explanation : As ‘d’ comes after ‘l’ in Order, thus words[0] > words[1], hence the sequence is unsorted.
'''


def verifyingAlienDictionary(words, order):
    records = []

    #Add to records array as tuple if char from side by side words are not matched

    # because we are comparing i to i+1 range is one less
    for i in range(len(words) - 1):
        for j in range(min(words[i], words[i+1])):
            if words[i][j] == words[i+1][j]:
                continue
            records.append([words[i][j], words[i+1][j]])                
            #we got mismtached char, break from the loop
            break
        
    if records == []:
        return False

    #now compare records with order
    for record in records:
        if order.index(record[0]) > order.index(record[1]):
            return True


    # now recor            


print(verifyingAlienDictionary(["hello", "leetcode"], "habcldefgijkmnopqrstuvwxyz"))