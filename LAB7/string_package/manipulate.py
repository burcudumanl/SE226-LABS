def reverse_string(s):
    return "".join(reversed(s))
def capitalize_words(s):
    return " ".join(s.capitalize())
def remove_punctuation(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))
