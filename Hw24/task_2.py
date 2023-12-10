from faker import Faker


def generate_random_words(num_words: int):
    if type(num_words) != int or num_words > 10000:
        raise ValueError("The number of words must be less or equal 10,000, type(num_words) must be int")
    fake = Faker()
    while num_words > 0:
        yield fake.unique.word()
        num_words -= 1


print(list(generate_random_words(10)))
