def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
    
def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    
def heron(a, b, c):
    s = (a + b + c) / 2
    return (s * (s-a) * (s-b) * (s-c)) ** 0.5

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
    

a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

print("\nCan it be a triangle?")
if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')
print("\nIs it a right triangle?", is_a_right_triangle(a, b, c), sep="\n")
print("\nArea of Triangle:", area_of_triangle(a, b, c))
