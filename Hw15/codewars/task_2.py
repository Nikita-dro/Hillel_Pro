# Instructions
#
# Implement a function which when given the arguments
#
#     Direction to which to cycle the current value
#     List of values
#     Current value
#
# returns the value next to current value in the specified direction.
#
# The function should pick the next value from the other side of the list in case there are no values
# in the given direction.
# Examples
#
# # Given the direction 1, returns the value next to 1 on the right
# cycle(1, [1,2,3], 1)   # => 2
#
# # Given the direction -1 and value 1, wraps around list returning the last element
# cycle(-1, [1,2,3], 1)  # => 3
#
# # 0 does not exist in the list, returns null
# cycle(1, [1,2,3], 0)   # => null
#
# # Corner case: multiple instances of given value, picks next relative to first occurrence
# cycle(1, [1,2,2,3], 2) # => 2
def cycle(direction, values, current):
    if current not in values:
        return None

    index = values.index(current)
    if direction == 1:
        next_index = (index + 1) % len(values)
    elif direction == -1:
        next_index = (index - 1) % len(values)

    return values[next_index]


assert (cycle(-1, [*range(0, 7)], 9) is None)
assert (cycle(1, [*range(0, 23, 2)], 17) is None)
assert (cycle(-1, [*range(0, 23, 2)], 11) is None)
assert (cycle(-1, [*range(0, 50, 4)], 8) == 4)
assert (cycle(-1, [*range(0, 50, 4)], 28) == 24)
assert (cycle(-1, [*range(0, 50, 4)], 0) == 48)
assert (cycle(1, [*range(0, 50, 7)], 28) == 35)
assert (cycle(1, [*range(0, 110, 8)], 64) == 72)
assert (cycle(1, [*range(0, 70, 3)], 15) == 18)
assert (cycle(1, [*range(0, 70, 3)], 69) == 0)

