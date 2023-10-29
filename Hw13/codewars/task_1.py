# Given an integral number, determine if it's a square number:
#
# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words,
# it is the product of some integer with itself.
#
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.
# Examples
#
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false

import math


def is_square(n):
    if n >= 0:
        root = math.isqrt(n)
        return False if root ** 2 != n else True
    else:
        return False


assert (is_square(-1) == False)
assert (is_square(0) == True)
assert (is_square(3) == False)
assert (is_square(4) == True)
assert (is_square(25) == True)
assert (is_square(26) == False)
