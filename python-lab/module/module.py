__counter = 0

def suml(lst):
    global __counter
    __counter += 1
    the_sum = 0
    for x in lst:
        the_sum += x
    return the_sum

def prodl(lst):
    global __counter
    __counter += 1
    prod = 1
    for x in lst:
        prod *= x
    return prod

if __name__ == '__main__':
    print("I prefer to be a module, but i can do some tests for you.")
    l = [i+1 for i in range(5)]
    print(suml(l) == 15)
    print(prodl(l) == 120)

