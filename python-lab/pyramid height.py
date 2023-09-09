blocks = int(input("Enter the number of blocks: "))

counter = 0
height = 0
total_blocks = 0

while total_blocks <= blocks:

    total_blocks = total_blocks + counter + 1

    counter += 1

    height = counter - 1

print("The height of the pyramid:", height)

"""
Sample input: 6, 20, 1000, 2

Expected output: 3, 5, 44, 1
"""
