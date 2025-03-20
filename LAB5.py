import random
import string

letter_replacements = {}
for _ in range(5):
    letter = input("Enter a lowercase character: ")
    replacements = set()
    while len(replacements) < 3:
        rep_char = input(f"Enter a replacement for '{letter}': ")
        if len(rep_char) == 1 and rep_char not in replacements:
            replacements.add(rep_char)
        else:
            print("Replacement must be unique and a single character!")
    letter_replacements[letter] = list(replacements)

passwords = []
for _ in range(5):
    password = ''.join(random.choices(string.ascii_lowercase, k=15))
    passwords.append(password)

categorized_passwords = {'strong': [], 'weak': []}

for pwd in passwords:
    replaced_count = 0
    new_pwd = []

    for ch in pwd:
        if ch in letter_replacements:
            new_pwd.append(random.choice(letter_replacements[ch]))
            replaced_count += 1
        else:
            new_pwd.append(ch)

    new_pwd = ''.join(new_pwd)

    if replaced_count > 4:
        categorized_passwords['strong'].append(new_pwd)
    else:
        categorized_passwords['weak'].append(new_pwd)

print("\nGenerated Passwords:")

print("\nSTRONG PASSWORDS:")
if categorized_passwords['strong']:
    for pwd in categorized_passwords['strong']:
        print(pwd)
else:
    print("No strong passwords generated. Try increasing the number of selected letters!")

print("\nWEAK PASSWORDS:")
for pwd in categorized_passwords['weak']:
    print(pwd)
