# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cvpF64tdnmF1KSNRNcWqRcXZt6W81EZp
"""

my_list = [1, 'hello', 3.14, True]
print("Original List: ",my_list)

print(dir(str))







my_list.append('world')
print("List after appending 'world':",my_list)

my_tuple = (1,'apple',3.14,False)
print()

my_list = [1, 'hello', 3.14, True]
print("Original List: ",my_list)
my_list.append('world')
print("List after appending 'world':",my_list)
my_tuple = (1,'apple',3.14,False)
print("Original Tuple:", my_tuple)
print("First element of the tuple:", my_tuple[0])
print("Second element of the tuple:", my_tuple[1])

print("\nIterating through the tuple using a for loop and index:")
for i in range(len(my_tuple)):
  print(f"Element at index {i}: {my_tuple[i]}")

count = 0
while count < 5:
  print(f"Count is {count}")
  count += 1
print("Loop finished!")

number = 10

if number > 0:
    print(f"{number} is a positive number.")
else:
    print(f"{number} is not a positive number.")