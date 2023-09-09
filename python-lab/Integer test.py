def read_int(prompt, min, max):
    while True:
        try:
            v = int(input(prompt))
            if v<min or v>max:
                raise
            else:
                return v
        except ValueError:
            print("Error: wrong input")
            continue
        except:
            print("Error: the value is not within permitted range (-10..10)")
            continue
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

"""
Test data:
Enter a number from -10 to 10: 100
Error: the value is not within permitted range (-10..10)
Enter a number from -10 to 10: asd
Error: wrong input
Enter number from -10 to 10: 1
The number is: 1
"""
