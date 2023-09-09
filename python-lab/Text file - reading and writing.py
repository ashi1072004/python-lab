from os import strerror
import sys

try:
    stream = open('newtext.txt', 'w')
    for i in range(10):
        stream.write('line # ' + str(i+1) + '\n')
    stream.close()
    count = lcount = 0
    #s = open("C:/Users/HAM TV/Desktop/New Text Document.txt", "rt", encoding = "utf-8")
    """
    #To read file content as a whole
    
    content = s.read()
    print(content)
    for ch in content:
        print(ch, end='')
        count += 1
    """
    """
    #Read character by character
    
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        count += 1
        ch = s.read(1)
    """
    """
    #Read line by line
    
    line = s.readline()
    while line != '':
        lcount += 1
        for ch in line:
            print(ch, end='')
            count += 1
        line = s.readline()
    """
    """
    #Read lines not more than a specified number of bytes at once.

    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcount += 1
            for ch in line:
                print(ch, end='')
                count += 1
        lines = s.readlines(10)
    """
    for i in open('newtext.txt', 'r'):
        print(i, end='')
    for line in open("C:/Users/HAM TV/Desktop/New Text Document.txt", "rt"):
        lcount += 1
        for ch in line:
            print(ch, end='')
            count += 1
    #s.close()
    print("\n\nCharacters in file:", count)
    print("Lines in file:     ", lcount)
except IOError as exc:
    sys.stderr.write("Error message")
    print("I/O error occurred: ", strerror(exc.errno))
