input = input('Enter Series of words to create an acronym: ')

acroSplit = input.split(' ')

output = ''

for i in acroSplit:
    val = i[:1]
    output = output + val.upper()

print(output)