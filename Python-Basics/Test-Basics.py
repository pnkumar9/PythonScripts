#!/usr/binenv python3.6

def somefun(string):

    print (len(string))
    print (string[-1])

    left = 0
    right = len(string)-1

    while left < right:
        print({f"left: {left} right: {right}"})
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1
    
    return True
	

print(somefun("Kumar"))