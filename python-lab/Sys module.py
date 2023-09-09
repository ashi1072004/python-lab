import sys

if len(sys.argv) != 3:
  raise ValueError("Please provide your name and age")

print(f' Your name is {sys.argv[1]} and your age is {sys.argv[2]}')
