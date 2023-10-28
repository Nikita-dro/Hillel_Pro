# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
# but exactly 4 digits or exactly 6 digits.
#
# If the function is passed a valid PIN string, return true, else return false.
# Examples (Input --> Output)
#
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


assert (validate_pin("1") == False)
assert (validate_pin("12") == False)
assert (validate_pin("123") == False)
assert (validate_pin("12345") == False)
assert (validate_pin("1234567") == False)
assert (validate_pin("-1234") == False)
assert (validate_pin("-12345") == False)
