from string_package import reverse_string, capitalize_words, remove_punctuation
from string_package import count_characters, count_words, average_word_length
sentence=input("Enter a sentence: ")
print(f"Reversed version of the sentence: {reverse_string(sentence)}")
print(f"Capitalized version of the sentence: {capitalize_words(sentence)}")
remove_punctuation(sentence)
print(f"Count of the characters in the sentence: {count_characters(sentence)}")
print(f"Count of the words in the sentence: {count_words(sentence)}")
average_word_length(sentence)
print(f"Average word length of the sentence: {average_word_length(sentence)}")
