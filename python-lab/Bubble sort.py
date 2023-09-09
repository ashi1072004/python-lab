my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)

"""
my_list.sort()  built-in method to sort a list.
reverse()       to reverse the list,
"""

"""
def isAscending(arr):
   n = len(arr)
   if n == 1 or n == 0:
       return True
   return arr[0] <= arr[1] and isAscending(arr[1:])
 
arr=[1,4,2,3,5]
print(isAscending(arr))
 
arr=[1,2,3,4,5]
print(isAscending(arr))

#Output:
#False
#True
"""
