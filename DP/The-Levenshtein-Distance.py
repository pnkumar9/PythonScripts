'''
The Levenshtein Distance
The Levenshtein distance is a metric to measure how apart are two sequences of words. 
In other words, it measures the minimum number of edits that you need to do to change a one-word sequence 
into the other. 
These edits can be insertions, deletions or substitutions.
 This metric was named after Vladimir Levenshtein, who originally considered it in 1965.

s1 = "abc"
s2 = "yabd"
it needs two edit
The formal definition of the Levenshtein distance between two strings a and b can be seen as follows:

Levenshtein-distance.png

r= row
c= column

r-1,c-1 ==> diagonal cell left up to r,c
r-1,c ==> cell just above current one r,c
r,c-1 ==> left cell to r,c
'''

def levenshteinDistance(str1, str2):
    edits = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    
    #create first column
    for i in range(1, len(str2)+1):
        edits[i][0] = edits[i-1][0] + 1
        
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                edits[i][j] = edits[i-1][j-1]
            else:
                edits[i][j] = 1+ min(edits[i-1][j-1], edits[i-1][j], edits[i][j-1])
                
    return edits[-1][-1]	
        

print(levenshteinDistance("abc", "yabd"))        