import numpy as np
from numpy.testing import assert_equal


def test_numpy():
    # Create a 2 (rows) x 3 (columns) matrix of zeros (remember 2 sets of brackets because the argument is either an int
    # for a 1-D array or a tuple)
    zeros = np.zeros((2, 3))
    assert_equal(zeros, ([0, 0, 0],
                         [0, 0, 0]))

    # Create a 2 x 3 matrix of ones (remember 2 sets of brackets)
    ones = np.ones((2, 3))
    assert_equal(ones, ([1, 1, 1],
                        [1, 1, 1]))

    # Creates a 3 x 3 Identity matrix
    im = np.eye(3)
    assert_equal(im, ([1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]))

    # Convert a normal array to numpy array
    arr = [[1, 2], [3, 4]]
    np_arr = np.array(arr)
    assert_equal(np_arr, ([[1, 2], [3, 4]]))

    # Can index into a N-D array using multiple square brackets or commas inside the square brackets (although commas
    # inside brackets does not work for normal Python arrays)
    na = np.array(arr)
    assert na[0][0] == 1

    # Can put conditions inside subscript
    np_range = np.arange(0, 5)
    updated_np_range = np_range[np_range < 3]
    assert_equal(updated_np_range, ([0, 1, 2]))

    # Can use many universal functions which operate on an element-by-element basis, e.g. add 5
    arr_plus_five = np_arr + 5
    assert_equal(arr_plus_five, ([[6, 7], [8, 9]]))

    # Two ways to get dimensions of numpy array
    assert_equal(np.shape(np_arr), ([2, 2]))
    assert_equal(np_arr.shape, ([2, 2]))

    flat = np.ravel(np_arr)
    assert_equal(flat, ([1, 2, 3, 4]))
