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
    arr = [[1, 2, 3], [4, 5, 6]]
    np_arr = np.array(arr)
    assert_equal(np_arr, ([[1, 2, 3], [4, 5, 6]]))

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
    assert_equal(arr_plus_five, ([[6, 7, 8],
                                  [9, 10, 11]]))

    # Two ways to get dimensions of numpy array
    assert_equal(np.shape(np_arr), ([2, 3]))
    assert_equal(np_arr.shape, ([2, 3]))

    flat = np.ravel(np_arr)
    assert_equal(flat, ([1, 2, 3, 4, 5, 6]))

    # Transpose a matrix
    transpose = np_arr.T
    assert_equal(transpose, ([1, 4],
                             [2, 5],
                             [3, 6]))

    # Add two matrices together
    together = np.add(np_arr, np_arr)
    assert_equal(together, ([2, 4, 6],
                            [8, 10, 12]))


def test_numpy_multiplication():
    np_arr = np.array([[1, 2],
                       [3, 4],
                       [5, 6]])

    # Multiplication by scalar, e.g. 3
    result = np.multiply(np_arr, 3)
    assert_equal(result, ([[3,  6],
                           [9,  12],
                           [15, 18]]))

    # Multiplication by vector
    vector = np.array([[1], [2]])
    result = np_arr.dot(vector)
    assert_equal(result, ([[5], [11], [17]]))

    # Multiplication by matrix
    matrix = np.array([[1, 3],
                       [2, 4]])
    result = np_arr.dot(matrix)
    assert_equal(result, ([[5, 11],
                           [11, 25],
                           [17, 39]]))
