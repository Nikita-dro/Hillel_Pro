class frange:
    def __init__(self, *args):
        if len(args) == 1:
            self.left = 0.0
            self.right = args[0]
            self.step = 1.0
        elif len(args) == 2:
            self.left = args[0]
            self.right = args[1]
            self.step = 1.0
        elif len(args) == 3:
            self.left = args[0]
            self.right = args[1]
            self.step = args[2]
        else:
            raise TypeError('Must be at most 3 arguments')
        self.current = self.left

    def __next__(self):
        if (self.step > 0 and self.current >= self.right) or (self.step < 0 and self.current <= self.right):
            raise StopIteration
        else:
            value = self.current
            self.current += self.step
            return value

    def __iter__(self):
        return self


for i in frange(1, 100, 3.5):
    print(i)

assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')