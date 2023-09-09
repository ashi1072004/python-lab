text1 = input('Enter a text: ')
text2 = input('Enter another text: ')

if text1 == '' or text2 == '':
    print('Not Anagrams')
else:
    lst1 = sorted(text1.lower())
    lst2 = sorted(text2.lower())
    text1 = ''
    text2 = ''
    for char in lst1:
        if not char.isalpha():
            continue
        else:
            text1 += char
    for char in lst2:
        if not char.isalpha():
            continue
        else:
            text2 += char

    #To Debug:
    #print(text1)
    #print(text2)

    if text1 == text2:
        print('Anagrams')
    else:
        print('Not Anagrams')
