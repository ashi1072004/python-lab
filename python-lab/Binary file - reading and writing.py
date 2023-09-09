from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
    """
    #for loop can still work without opening file in rb mode
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()
    """
    #Here read() method creats an immutable object of bytes class
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    #This read() method reads only first five bytes of the file.
    #data = bytearray(bf.read(5))

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

"""
def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2
    return inner


b_tag = tag('<b>')
print(b_tag('Monty Python'))
"""
