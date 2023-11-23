def sum_of_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    total_length = 0
    current_start, current_end = sorted_intervals[0]

    for start, end in sorted_intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            total_length += current_end - current_start
            current_start, current_end = start, end

    total_length += current_end - current_start

    return total_length


assert (sum_of_intervals([(1, 5)]) == 4)
assert (sum_of_intervals([(1, 5), (6, 10)]) == 8)
assert (sum_of_intervals([(1, 5), (1, 5)]) == 4)
assert (sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)
assert (sum_of_intervals([(-1_000_000_000, 1_000_000_000)]) == 2_000_000_000)
assert (sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]) == 100_000_030)
