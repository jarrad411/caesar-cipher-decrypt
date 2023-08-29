import string
from collections import Counter

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((ord(char) - shift - ord('a') + 26) % 26 + ord('a'))
            elif char.isupper():
                decrypted_char = chr((ord(char) - shift - ord('A') + 26) % 26 + ord('A'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

def find_shift(encrypted_text):
    frequencies = Counter(filter(str.isalpha, encrypted_text.lower()))
    most_common_letter = frequencies.most_common(1)[0][0]
    shift = ord(most_common_letter) - ord('e')
    return shift

input_file = "input.txt"
with open(input_file, "r") as file:
    encrypted_text = file.read()

shift = find_shift(encrypted_text)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print("Decrypted Text:", decrypted_text)
print("Found Shift Value:", shift)

