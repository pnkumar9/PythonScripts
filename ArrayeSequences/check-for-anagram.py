#!/usr/bin/env pytho3.6
'''
replace spaces and lower all the words
sort both the strings
compare both the strings
'''
def check_for_anagram(str1, str2):
    print(str1,str2)
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    if len(str1) != len(str2):
        return False
    return (sorted(str1) == sorted(str2))
#print(check_for_anagram('god','dog'))
#print(check_for_anagram('clint eastwood','old west action'))
#print(check_for_anagram('clinton eastwood','old west action'))

'''
check the frequency of each letter in both the strings
if count is same, its anagram
Use dictionary to keep every letter count
'''
def check_for_anagram_method2(str1, str2):
        print(str1,str2)
        str1 = str1.replace(" ","").lower()
        str2 = str2.replace(" ","").lower()

        count_dict = {}
        for letter in str1:
            if letter in count_dict:
                count_dict[letter] += 1
                #print(f" 1st if {letter}")
            else:
                count_dict[letter] = 1
                #print(f" 2nd if {letter}")

        # for str2 subtract the count, if count is zero then its anagram
        for letter in str2:
            if letter in count_dict:
                count_dict[letter] -= 1
            else:
                count_dict[letter] = 1

        for k in count_dict:
            if count_dict[k] != 0:
                return False

        return True
#print(check_for_anagram_method2('clint eastwood', 'old west action'))

from collections import Counter  
def check_for_anagram_using_Counter(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = s.replace(" ","").lower()
        t = t.replace(" ","").lower()
        print(f"s: {s} t: {t}")        
        return Counter(s) == Counter(t)

print(check_for_anagram_using_Counter('clint eastwood', 'old west action'))
print(check_for_anagram_using_Counter('clint eastwood', 'old west action2'))         