# Suppose you have 4 numbers: 0, 9, 6, 4 and 3 strings composed with them:
#
# s1 = "6900690040"
# s2 = "4690606946"
# s3 = "9990494604"
#
# Compare s1 and s2 to see how many positions they have in common:
# 0 at index 3, 6 at index 4, 4 at index 8 : 3 common positions out of ten.
#
# Compare s1 and s3 to see how many positions they have in common:
# 9 at index 1, 0 at index 3, 9 at index 5 : 3 common positions out of ten.
#
# Compare s2 and s3. We find 2 common positions out of ten.
#
# So for the 3 strings we have 8 common positions out of 30 ie 0.2666... or 26.666...%
#
# Given n substrings (n >= 2) in a string s our function pos_average will calculate the average percentage
# of positions that are the same between the (n * (n-1)) / 2 sets of substrings taken amongst the given n substrings.
# It can happen that some substrings are duplicate but since their ranks are not the same in s they are considered
# as different substrings.
#
# The function returns the percentage formatted as a float with 10 decimals but the result is tested at 1e.
# -9 (see function assertFuzzy in the tests).
# Example:
#
# Given string s = "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490" composing
# a set of n = 10 substrings (hence 45 combinations), pos_average returns 29.2592592593.
#
# In a set the n substrings will have the same length ( > 0 ).

def pos_average(s):
    substrings = s.split(", ")
    total_positions = 0
    total_combinations = 0

    for i in range(len(substrings)):
        for j in range(i + 1, len(substrings)):
            common_positions = sum(a == b for a, b in zip(substrings[i], substrings[j]))

            total_positions += common_positions
            total_combinations += len(substrings[i])

    average_percentage = (total_positions / total_combinations) * 100

    return round(average_percentage, 10)


assert (pos_average("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096") == 26.6666666667)
assert (pos_average("444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490") == 29.2592592593)
assert (pos_average("449404, 099090, 600999, 694460, 996066, 906406, 644994, 699094, 064990, 696046") == 24.4444444444)
assert (pos_average("660999, 969060, 044604, 009494, 609009, 640090, 994446, 949940, 046999, 609444") == 22.9629629630)
assert (pos_average("996060, 606494, 964494, 460409, 609449, 969600, 960944, 960006, 666049, 090996") == 24.8148148148)
assert (pos_average("40664064, 60460960, 00669664, 94040464, 04006499, 00466666, 90966460, 64494990") == 29.0178571429)
assert (pos_average("64040600, 64464440, 60006040, 49609906, 46664409, 99464446, 90446964, 96940090") == 20.5357142857)
assert (pos_average("99494909, 60004094, 60090496, 64664669, 49909604, 49999064, 46009964, 44494444") == 25.4464285714)
assert (pos_average("46904946, 60996660, 64040460, 40449469, 46440460, 96090699, 06600440, 44046966") == 27.6785714286)
assert (pos_average("46099969, 64096999, 44949949, 06409969, 09064604, 90490494, 04600696, 94469969") == 25.8928571429)
assert (pos_average("4444444, 4444444, 4444444, 4444444, 4444444, 4444444, 4444444, 4444444") == 100)
assert (pos_average("0, 0, 0, 0, 0, 0, 0, 0") == 100)
assert (pos_average("0, 0, 1") == 33.3333333333)
