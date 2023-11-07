# In this challenge you will be given a list similar to the following:
#
# [[3], 4, [2], [5], 1, 6]
#
# In words, elements of the list are either an integer or a list containing a single integer.
# If you try to sort this list via sorted([[3], 4, [2], [5], 1, 6]), Python will whine about not being able
# to compare integers and lists.
#
# However, us humans can clearly see that this list can reasonably be sorted according
# to "the content of the elements" as:
# [1, [2], [3], 4, [5], 6]
#
# Create a function that, given a list similar to the above, sorts the list according to the "content of the elements".
#
# Examples
#
# [4, 1, 3] ➞ [1, 3, 4]
#
# [[4], [1], [3]] ➞ [[1], [3], [4]]
#
# [4, [1], 3] ➞ [[1], 3, 4]
#
# [[4], 1, [3]] ➞ [1, [3], [4]]
#
# [[3], 4, [2], [5], 1, 6] ➞ [1, [2], [3], 4, [5], 6]
def sort_it(lst):
    return sorted(lst, key=lambda x: x if isinstance(x, int) else x[0])


assert (sort_it([4, 1, 3]) == [1, 3, 4])
assert (sort_it([[4], [1], [3]]) == [[1], [3], [4]])
assert (sort_it([4, [1], 3]) == [[1], 3, 4])
assert (sort_it([[4], 1, [3]]) == [1, [3], [4]])
assert (sort_it([[3], 4, [2], [5], 1, 6]) == [1, [2], [3], 4, [5], 6])
assert (sort_it([[3], 7, [9], [5], 1, 6]) == [1, [3], [5], 6, 7, [9]])
assert (sort_it([[3], 7, [9], [5], 1, 6, [0]]) == [[0], 1, [3], [5], 6, 7, [9]])