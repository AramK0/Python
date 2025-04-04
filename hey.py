import random
import string


chars = " " + string.punctuation + string.ascii_letters + string.digits

chars = list(chars)
key = chars.copy()

random.shuffle(key)

#Encryption
plain_text = input("Enter a text to be encrypted: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original text: {plain_text}")
print(f"Encrypted text: {cipher_text}")

#Decryption
cipher_text = input("Enter a text to be encrypted: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted text: {cipher_text}")
print(f"Original text: {plain_text}")

