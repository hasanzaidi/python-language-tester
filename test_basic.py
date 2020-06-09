def test_operators():
    # 3^2
    power = 3**2
    assert power == 9

    # Floor division
    div = 9 // 2
    assert div == 4

    # Normal division
    div_normal = 9 / 2
    assert div_normal == 4.5

    # Can find type using type
    i = 123
    t = type(i)
    assert t == int

    # Can validate type
    is_str = isinstance("hello", str)
    assert is_str == True

    # Ternary operator
    val = True
    result = 'a' if val else 'b'
    assert result == 'a'

    hit_exception = False
    try:
        my_dict = {}
        del my_dict['a']
    except KeyError as ex:
        hit_exception = True
    assert hit_exception == True


def test_strings():
    accuracy = 2
    message = ("Accuracy: {}".format(accuracy))
    assert message == "Accuracy: 2"

    # Can index into a String like an array
    my_string = "abc"
    char = my_string[1]
    assert char == "b"

    # Convert unicode number to character
    char = chr(190)
    assert char == "¾"

    # Reverse of chr
    num = ord('¾')
    assert num == 190


def test_io():
    # Write a String to a file
    file = open('important_data.txt', "w")
    file.write('The secret password is 12345')
    file.close()

    # Write a String to a file using context managers, which doesn't require close line
    with open('important_data_no_close.txt', 'w') as f:
        f.write('The secret password is 12345')

    with open('important_data_no_close.txt', 'r') as f:
        file_contents = f.read()
        assert file_contents == "The secret password is 12345"
