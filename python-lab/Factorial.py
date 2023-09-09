"""
If, n! = 1 × 2 × 3 × ... × n-1 × n
Then, (n-1)! = 1 × 2 × 3 × ... × n-1
So, n! = (n-1)! × n
"""
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

for n in range(1, 6):
    print(n, factorial_function(n))
