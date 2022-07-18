import string
import re


def word_counter(text):
    words_punctuation = "-'"
    pattern = "[" + words_punctuation + "]"
    punctuation = re.sub(pattern, "", string.punctuation)

    text_without_punctuation = "".join([char if char not in punctuation else " " for char in text])

    list_of_words = text_without_punctuation.lower().split()
    list_of_words_without_punctuation = list(filter(lambda x: x not in words_punctuation, list_of_words))
    count = len(list_of_words_without_punctuation)
    return count
