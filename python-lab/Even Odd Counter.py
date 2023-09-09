odd_numbers = 0
even_numbers = 0

number = int(input("Enter a number or type 0 to stop: "))

while number:
    if number % 2:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Enter a number or type 0 to stop: "))

print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)
