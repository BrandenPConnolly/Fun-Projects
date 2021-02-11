'''
Creator: Branden
Date: 2021-02-11

Purpose: determines if words in a comma delimited list are palindromes
'''
# input comma delimited list of words
input = 'radar, madam, hello, ready, mayam, abcdeedcba'

def cleanandsplit(n):
    '''
    inputs a comma delimited list \n
    outputs a split list \n
    removes spaces from list
    '''
    clean = n.replace(' ','')
    split = clean.split(',')

    return split

def inPalindrome(n):
    '''
    inputs a word \n
    no outputs \n
    determines if inputted word is a palindrome \n
    '''
    lenN = len(n)
    halflen = lenN/2
    roundhalflen = lenN - .5
    check1 = 0
    check2 = -1
    match = 0
    
    if  lenN%2 == 0:
        while check1 < halflen:
            if n[check1] == n[check2]:
                match += 1
            else:
                print(n+ ' is not a palindrome')
                break
            
            check1 +=1 
            check2 -=1
        if match == halflen:
            print(n + ' is a palindrome')
    else:
        while check1 < int(roundhalflen):
            if n[check1] == n[check2]:
                match += 1
            else:
                print(n+ ' is not a palindrome')
                break
            
            check1 +=1 
            check2 -=1
        if match == int(roundhalflen):
            print(n + ' is a palindrome')

wordlist = cleanandsplit(input)

for i in wordlist:
    inPalindrome(i)