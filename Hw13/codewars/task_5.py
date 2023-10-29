# You might know some pretty large perfect squares. But what about the NEXT one?
#
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
#
# If the parameter is itself not a perfect square then -1 should be returned.
# You may assume the parameter is non-negative.
#
# Examples:(Input --> Output)
#
# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square
import math


def find_next_square(sq):
    sqrt_num = math.isqrt(sq)
    if sqrt_num ** 2 == sq:
        return (sqrt_num + 1) **2
    else:
        return -1


assert (find_next_square(121) == 144)
assert (find_next_square(625) == 676)
assert (find_next_square(319225) == 320356)
assert (find_next_square(15241383936) == 15241630849)
assert (find_next_square(155) == -1)
assert (find_next_square(342786627) == -1)