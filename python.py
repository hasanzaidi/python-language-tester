# Get the length of an array
my_list = [2, 4, 6, 8, 10]
len(my_list)
#
# # Multiply 3 to the power of 2
# 3**2
#
# # Floor division - divides two numbers and gets rid of the remainder. Equivalent to Java's integer division
# 9//2
#
# # Throwing an exception
# if len(items) == 0:
# 	raise ValueError("median() arg is an empty sequence")
#
# # Remove key from a dictionary
# del a['mykey']
#
# # Check if a key is in a dictionary
# d = {'a': 1, 'b': 2}
# 'a' in d
# # >>True
#
# # Check if a value is in a list
# languages = ['Java', 'C++', 'Go', 'Python', 'JavaScript']
# if 'Python' in languages:
#     print('Python is there!')
#
# # To create an empty dictionary
# ds = dict()
#
# # Get the last element in a Python array (negative indices means from the end. So -1 is last element, -2 is 2nd to last element, etc)
# a = [1, 2, 3]
# b = a[-1]
# >>3
#
# # Get the first two elements in a Python array
# a = [1, 4, 9]
# b = a[:2]
# >> [1, 4]
#
# # Tuple is like an array in that it holds a list of values but it is immutable (you can't change it afterwards)
# a = (1, 4, 9)
# a[0] = 2
# >> ERROR
#
# # Can do something called tuple unpacking
# x = [(1,2),(3,4)]
# for a,b in x:
# 	print(a)
# 	print(b)
# >> 1,2,3,4
#
# # Use enumerate if you want to get the index of items in a list
# for idx, val in enumerate(my_list):
#     print('idx: {}, value: {}'.format(idx, val))
#
# # Append adds an item to a list
# a = [1, 4, 9]
# a.append(10)
#
# # Set is like an array but adding duplicate values will have no effect
# a = {1, 4, 9}
# a.add(4)
# >> [Does nothing]
#
# # Can reverse a list using
# mylist = [1, 2, 3]
# reversed = mylist[::-1]
#
# # Write a String to a file
# file = open('important_data.txt', "w")
# file.write('The secret password is 12345')
# file.close()
#
# # Write a String to a file using context managers
# with open('important_data.txt', 'w') as f:
# 	f.write('The secret password is 12345')
#
# # Write a String to a file
# file = open("newfile.txt", "w")
# file.write(str_msg)
# file.close()
#
# # Print type of variable:
# i = 123
# type(i)
#
# # Printing strings
# print("Accuracy: {}".format(accuracy))
#
# # Python list comprehension example to double all the numbers in a list
# mylist = [1, 2, 3]
# doubled = [num * 2 for num in mylist]
#
# # Python nested list comprehension example to double all the numbers in a list of lists
# mylistoflists = [[1,2,3], [4,5,6], [7,8]]
# doubled = [[num * 2 for num in mylist] for mylist in mylistoflists]
# >> [[2, 4, 6], [8, 10, 12], [14, 16]]
#
# # Can use "map" function to run a function against every value in the list
# def times3(num): return num*3
# seq = [1, 2, 3]
# list(map(times3, seq))
# >> [3, 6, 9]
#
# # And can use Lambas to make it less verbose
# seq = [1, 2, 3]
# list(map(lambda num: num*3, seq))
# >> [3, 6, 9]
#
# # "filter" also operates on all values in a list, but filters out everything which does not match a condition
# seq = [1, 2, 3]
# list(filter(lambda num: num%2 ==0, seq))
# >> [2]
#
# # Adds up a list of numbers
# seq = [2, 1, 3, 4, 7, 11, 18]
# total = sum(seq)
#
# # Pass is a null operation (i.e. nothing happens). Useful to use temporarily as body for methods until they are fleshed out.
# pass
#
# # Loops through numbers in range 0 up to (but not including) 5
# for i in range(5):
# 	print(i)
#
# # Loops through numbers in range 3 up to (but not including) 6
# for i in range(3, 6):
# 	print(i)
#
# # _ can be used when you don't care about its value, e.g.
# for _ in range(10):
#     do_something()
#
# # Can index into a String like an array
# s = "abc"
# s[1]
# >> b
#
# # Python's ternary operator
# 'true' if True else 'false'
#
# # Reduce example which gets the total of a list of numbers
# import operator
# from functools import reduce
# values=[1, 2, 3]
# a = reduce(operator.add, values)
#
# # Returns true if the object is of the given type
# isinstance("hello", str)
