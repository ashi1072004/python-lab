text = input('Enter your message: ')
cipher = ''
shift = int(input("Enter shift value ranging from 1 to 25: "))
while shift<1 or shift>25:
    print('Invalid shift value.')
    shift = int(input("Enter shift value ranging from 1 to 25: "))
for char in text:
    if not char.isalpha():
        cipher += char
    else:
        if char == char.lower():
            char = chr(ord(char) + shift)
            if char > 'z':
                shift_again = ord(char) - ord('z')
                char = chr((ord('a') - 1) + shift_again)
        if char == char.upper():
            char = chr(ord(char) + shift)
            if char > 'Z':
                shift_again = ord(char) - ord('Z')
                char = chr((ord('A') - 1) + shift_again)
        cipher += char
print(cipher)

"""
Sample input:

abcxyzABCxyz 123
2

Sample output:

cdezabCDEzab 123

Sample input:

The die is cast
25

Sample output:

Sgd chd hr bzrs
"""
