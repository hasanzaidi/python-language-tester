import operator
from functools import reduce
from collections import Counter


def test_arrays():
    my_list = [2, 4, 6, 8, 10]
    length = len(my_list)
    assert length == 5

    # Initialise all elements in an array to a value
    all_ones = [-1 for i in range(5)]
    assert all_ones == [-1, -1, -1, -1, -1]

    # Checking in list
    languages = ['Java', 'C++', 'Go', 'Python', 'JavaScript']
    exists = 'Python' in languages
    assert exists == True

    # Get the last element (negative indices means from the end. So -1 is last element, -2 is 2nd to last element, etc)
    last = my_list[-1]
    assert last == 10

    # Get the first two elements
    first_two = my_list[:2]
    assert first_two == [2, 4]

    # Add an element to the end of an array
    my_list.append(12)
    assert my_list == [2, 4, 6, 8, 10, 12]

    # Can reverse list
    reversed_list = my_list[::-1]
    assert reversed_list == [12, 10, 8, 6, 4, 2]

    # Loops through numbers in range 0 up to (but not including) 5
    total = 0
    for i in range(5):
        total = total + i
    assert total == 10

    # Loops through numbers in range 3 up to (but not including) 6
    total = 0
    for i in range(3, 6):
        total = total + i
    assert total == 12

    # Can get index in list using enumerate
    strings = ""
    for idx, val in enumerate([9, 8, 7]):
        strings = strings + ('i={} v={}, '.format(idx, val))
    assert strings == "i=0 v=9, i=1 v=8, i=2 v=7, "

    # The counter class counts values in a list:
    colors = ["red", "red", "green", "yellow", "yellow", "red", "black"]
    color_counts = Counter(colors)
    assert color_counts == Counter({'red': 3, 'yellow': 2, 'green': 1, 'black': 1})


def test_func_programming():
    # Reduce example which gets the total of a list of numbers
    my_list = [1, 2, 3]
    total = reduce(operator.add, my_list)
    assert total == 6

    # Alternative way to sum up a list
    total = sum(my_list)
    assert total == 6

    # Python list comprehension example to double all the numbers in a list
    my_list = [1, 2, 3]
    doubled = [num * 2 for num in my_list]
    assert doubled == [2, 4, 6]

    # Python nested list comprehension example to double all the numbers in a list of lists
    my_list_of_lists = [[1, 2, 3], [4], [7, 8]]
    doubled_nested = [[num * 2 for num in sub_list] for sub_list in my_list_of_lists]
    assert doubled_nested == [[2, 4, 6], [8], [14, 16]]

    # Can use "map" function to run a function against every value in the list
    def times3(num): return num * 3
    times_3 = list(map(times3, my_list))
    assert times_3 == [3, 6, 9]

    # And can use Lambdas to make it less verbose
    times_3 = list(map(lambda num: num * 3, my_list))
    assert times_3 == [3, 6, 9]

    # "filter" also operates on all values in a list, but filters out everything which does not match a condition
    evens = list(filter(lambda num: num % 2 == 0, my_list))
    assert evens == [2]


def test_dictionaries():
    my_dict = {'a': 1, 'b': 2}

    # Delete from dictionary
    del my_dict['a']
    assert len(my_dict) == 1
    assert my_dict['b'] == 2

    # Checking in dictionary
    exists = 'b' in my_dict
    assert exists == True

    # Two ways to create a new dictionary
    new_dict1 = {}
    new_dict2 = dict()
    assert len(new_dict1) == 0
    assert len(new_dict2) == 0


def test_tuples():
    # Tuple is like an array in that it holds a list of values but it is immutable (you can't change it afterwards)
    my_tuple = (1, 4, 9)
    try:
        my_tuple[0] = 2
        assert False == False
    except TypeError:
        assert True == True

    # Can do something called tuple unpacking
    (start, end) = (1, 5)
    assert start == 1
    assert end == 5


def test_sets():
    # To create a new set
    new_set = set()
    assert len(new_set) == 0

    # Adding duplicate to set will have no effect
    my_set = {1, 4, 9}
    my_set.add(4)
    my_set.add(16)
    assert my_set == {1, 4, 9, 16}
