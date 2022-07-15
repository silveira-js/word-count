import string


def word_counter(text):
    cleaned_text = "".join([char if char not in string.punctuation else " " for char in text])
    text_list = cleaned_text.split()
    list_of_words = list(filter(lambda x: x.isalpha(), text_list))
    count = len(list_of_words)
    return count
