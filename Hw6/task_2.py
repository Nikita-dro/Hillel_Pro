class Colorizer:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'purple': '\033[95m',
        }
        if self.color not in colors:
            raise ValueError(f"Invalid color: {self.color}.")

        print(colors[self.color], end='')

    def __exit__(self, type, value, traceback):
        print('\033[0m', end='')


print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

with Colorizer('red'):
    print('printed in red')
print('printed in default color')
