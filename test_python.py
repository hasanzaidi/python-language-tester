import pytest
# import unittest
# from hamcrest import *
#
#
# class TestPython(unittest.TestCase):
#     def test_len(self):
#         my_list = [2, 4, 6, 8, 10]
#         len(my_list)
#         self.assertEqual(len(my_list), 5)
#         assert_that(len(my_list), equal_to(6))
#
#
# if __name__ == '__main__':
#     unittest.main()

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]