import contextlib


@contextlib.contextmanager
def colorizer(color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
    }

    reset = '\033[0m'
    if color not in colors:
        raise ValueError(f"Invalid color: {color}.")

    print(colors[color], end='')

    try:
        yield
    finally:
        print(reset, end='')


print('This is the default color')
print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

with colorizer('red'):
    print('printed in red')
print('printed in default color')
