class CustomMapIterator:
    def __init__(self, dict_info, func_1, func_2):
        self.dict_info = dict_info
        self.func_1 = func_1
        self.func_2 = func_2
        self.keys = list(dict_info.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            value = self.dict_info[key]
            self.index += 1
            return self.func_1(key), self.func_2(value)
        else:
            raise StopIteration


input_dict = {'car': 1, 'tree': 2, 'see': 3}


def func1(key):
    return key.upper()


def func2(value):
    return value * 2


custom_iterator = CustomMapIterator(input_dict, func1, func2)
for result in custom_iterator:
    print(result)
