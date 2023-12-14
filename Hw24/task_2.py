import nltk
from nltk.corpus import words
import random

nltk.download('words')


def generate_realistic_words(num_words: int):
    if type(num_words) != int or num_words > 10000:
        raise ValueError("The number of words must be less or equal 10,000, type(num_words) must be int")
    word_list = list(words.words())
    random.shuffle(word_list)
    unique_words = set(word_list)
    for word in list(unique_words)[:num_words]:
        yield word


print(len(list(generate_realistic_words(9999))))
print(len(set(generate_realistic_words(9999))))
