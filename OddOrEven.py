'''
Creator: Branden
Date: 2021-02-11

Purpose: Checks if inputed number is even or odd
'''

def numinput():
    n = input('Please Enter a Integer: ')
    return n


def evenodd(n):
    '''
    Input: any integer \n
    Output: If Number if even or odd (True or False) \n
    '''
    if n%2 == 0:
        tf = True
    else:
        tf = False
    
    return tf

def isInt(n,mess):
    '''
    Inputs Number and if message should display\n
    Outputs if number is an int \n
    '''
    try:
        int(n)
    except:
        if mess.upper() == 'Y':
            print('Not an integer, try again')
        tf = False
    else:
        tf = True
    return tf

def contInput(n):
    if isInt(n,'N') == True:
        Continue = input('Would You like to Continue (Y or N): ')
    else:
        Continue = input('Would you like to try again (Y/N): ')

    return Continue


def output(n):
    if isInt(n,'Y') == True:

        if evenodd(int(n)) == True:
            print('Even Number')
            Continue = contInput(n)
        else:
            print('Odd Number')
            Continue = contInput(n)
    else:
        Continue = contInput(n)
    
    return Continue

def main():
    tOrF = True #place holder
    InputNum = 9 #place holder
    Continue = 'Y' #starts as Y 

    while Continue.upper() == 'Y':
        InputNum = numinput()
        Continue = output(InputNum) 
    print('Ending Program...')

main()