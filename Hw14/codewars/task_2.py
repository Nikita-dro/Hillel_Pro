# Make a program that filters a list of strings and returns a list with only your friends name in it.
#
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
# Otherwise, you can be sure he's not...
#
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

def friend(names):
    return [name for name in names if len(name) == 4]


assert (friend(["Ryan", "Kieran", "Mark", ]) == ["Ryan", "Mark"])
assert (friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]) == ["Ryan"])
assert (friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]) == ["Jimm", "Cari", "aret"])
