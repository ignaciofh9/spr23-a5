#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

# Checks that the program outputs "99" for an input of "99 + 0"
assert run("99 + 0").output == "99"
# Checks that the program outputs "-3" for an input of "-3 * 1"
assert run("-3 * 1").output == "-3"
# Checks that the program outputs "100.5" for an input of "201 / 2"
assert run("201 / 2").output == "100.5"

print("All tests passed!")
###

print("All tests passed!")
