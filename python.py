# Code snippets which can't really be expressed in unit test

# Throwing an exception
items = [1, 2]
if len(items) == 0:
    raise ValueError("Empty list")

# Pass is a null operation (i.e. nothing happens). Useful to use temporarily as body for methods until they are fleshed
# out.
f = False
if f is True:
    pass
else:
    print("hello")
print("print line never gets called")

# _ can be used when you don't care about its value, e.g.
print()
for _ in range(5):
    print("hello world")


# To create a custom exception class
class CustomError(Exception):
    pass
