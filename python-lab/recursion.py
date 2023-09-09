"""
def dispn(n):
    if n == 0:
        return  # Base case
    print(n)
    dispn(n - 1)  # Tail Recursive Call


dispn(5)
#displays:
#5
#4
#3
#2
#1
"""

"""
def dispn(n):
    if n == 0:
        return  # Base case
    dispn(n - 1)  # Head Recursive Call
    print(n)


dispn(5)
#displays:
#1
#2
#3
#4
#5
"""

def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))

"""
res = 0
start = 1


def reverseDigits(num):
    global res
    global start
    if num > 0:
        reverseDigits(int(num / 10))
        res += (num % 10) * start
        start *= 10
    return res


print(reverseDigits(524))
"""
