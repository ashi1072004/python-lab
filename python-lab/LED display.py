digit0 = ("###","# #","# #","# #","###")
digit1 = ("  #","  #","  #","  #","  #")
digit2 = ("###","  #","###","#  ","###")
digit3 = ("###","  #","###","  #","###")
digit4 = ("# #","# #","###","  #","  #")
digit5 = ("###","#  ","###","  #","###")
digit6 = ("###","#  ","###","# #","###")
digit7 = ("###","  #","  #","  #","  #")
digit8 = ("###","# #","###","# #","###")
digit9 = ("###","# #","###","  #","###")
 
digitList = [digit0,digit1,digit2,digit3,digit4,digit5,digit6,digit7,digit8,digit9]
digits = input("Enter a value: ") 
for j in range(5):
    result = ""
    for i in digits:
        result += digitList[int(i)][j]+" "
        #print (result, sep="\n") , to debug
    print (result, sep="\n")

"""
representations = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###')
}

def seven_segment(number):
    digits = [representations[digit] for digit in str(number)]
    for i in range(5):
        print(" ".join(segment[i] for segment in digits))
number = int(input("Enter a value: "))
seven_segment(number)
"""
