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
    if  n == n[::-1]:
        print(n + ' is a palindrome')
    else:
        print(n + ' is not a palindrome')

wordlist = cleanandsplit(input)

for i in wordlist:
    inPalindrome(i)