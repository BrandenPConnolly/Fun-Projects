'''
Creator: Branden
Date: 2021-02-11

Purpose: Checks if inputed number is even or odd
'''



tOrF = True
InputNum = 9
Continue = 'Y'

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

def isInt(n):
    '''
    Inputs Number \n
    Outputs if number is an int \n
    '''
    try:
        int(n)
    except:
        print('Not an integer, try again')
        tf = False
    else:
        tf = True
    return tf

while Continue.upper() == 'Y':

    InputNum = input('Please Enter a Integer (rounds decimals): ')

    if isInt(InputNum) == True:

        if evenodd(int(InputNum)) == True:
            print('Even Number')
            Continue = input('Would You like to Continue (Y or N): ')
        else:
            print('Odd Number')
            Continue = input('Would You like to Continue (Y or N): ')
    else:
        Continue = input('Would you like to try again (Y/N): ')
    

print('Ending Program...')