import os as os
import string
import subprocess

indataop = 'C:/Users/Brand/OneDrive/Desktop/PythonFunProjects/wordcountertestfile.txt'

def enteroropen():
    eoro = input('Would you like to enter a string (Y/N): ')
    return eoro

def inputstring():
    a = input('Enter string that you want words counted in: ')
    return a

def openfile(a):
    with open(a,'r') as aa:
        text = aa.read()
    return text

def cleanandsplit(a):
    text = a.split(' ')

    cleanlist = []
    for i in text:
        textclean = ''.join(ch for ch in i if ch.isalnum())
        if len(textclean) > 0:
            cleanlist.append(textclean)    

    return cleanlist

def main():
    if enteroropen().upper() == 'Y':
        text = inputstring()
    else:
        print('Using test text file...')
        text = openfile(indataop)

    cleantext = cleanandsplit(text)
    print('string is ' + str(len(cleantext)) + ' words long')

main()