def new_format(string: str) -> str:
    try:
        number = int(string)
        formatted_number = format(number, ',d')
        return formatted_number.replace(',', '.')
    except ValueError:
        raise ValueError("Characters found in the text that are not numbers!")


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
