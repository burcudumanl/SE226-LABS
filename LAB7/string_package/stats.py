import string
def count_characters(s):
    b=s.split(" ")
    sum=0
    for c in b:
        sum+=len(c)
    return sum
def count_words(s):
    a=s.split(" ")
    return len(a)
def average_word_length(s):
    return count_characters(s) / count_words(s)