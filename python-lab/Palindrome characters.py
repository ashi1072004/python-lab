
text = input('Enter a line: ')
new_text = ''
reversed_text = ''

if text != '':
    for char in text:
        if not char.isalnum():
            continue
        elif char.isdigit():
            new_text += char
        else:
            char = char.lower()
            new_text += char
    reversed_text = ''.join(reversed(new_text))
    #To debug:
    #print(new_text)
    #print(reversed_text)
    if reversed_text:
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")
else:
    print("It's a palindrome.")

"""
def isPalindrome(s):
    return s == s[::-1]
    
s = input("Enter a word: ")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
"""
