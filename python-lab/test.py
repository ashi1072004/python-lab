def twoD(n):
   arr = [[0 for row in range(n)] for column in range(n)]
   for row in arr:
      print(" ".join(str(cell) for cell in row))
      print("")

if __name__ == '__main__':
   twoD(5)
"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
"""
"""
# Python code to demonstrate call by reference

def append_to_list(list1):
   list1.append(35)
   print("Inside Function: ", list1)
 
multiples_of_5 = [5,10,15,20,25,30]
append_to_list(multiples_of_5)
print("Outside Function: ", multiples_of_5)
"""
