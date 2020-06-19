import os.path
import datetime
from datetime import timedelta


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
    assert is_str is True

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
    assert hit_exception is True


def test_strings():
    accuracy = 2
    message = ("Accuracy: {}".format(accuracy))
    assert message == "Accuracy: 2"

    # Can index into a String like an array
    my_string = "abc"
    char = my_string[1]
    assert char == "b"

    # Convert unicode number to character
    char = chr(128512)
    assert char == "😀"

    # Reverse of chr
    num = ord('😀')
    assert num == 128512


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

    # Check if file exists
    file_exists = os.path.exists('important_data.txt')
    assert file_exists is True
    file_exists = os.path.exists('madeup_file.txt')
    assert file_exists is False


def test_dates():
    # Parse date
    parsed_date = datetime.datetime.strptime("Jun 21 at 16:40", '%b %d at %H:%M')
    assert parsed_date == datetime.datetime(1900, 6, 21, 16, 40)

    # Update part of the date
    updated_date = parsed_date.replace(year=2020)
    assert updated_date == datetime.datetime(2020, 6, 21, 16, 40)

    # Check date is in the past or future
    is_future = datetime.datetime(2030, 6, 21, 16, 40) > datetime.datetime.now()
    assert is_future is True
    is_past = datetime.datetime(2000, 6, 21, 16, 40) > datetime.datetime.now()
    assert is_past is False

    # Add some amount of days to date
    ten_days_later = updated_date + timedelta(days=10)
    assert ten_days_later == datetime.datetime(2020, 7, 1, 16, 40)

