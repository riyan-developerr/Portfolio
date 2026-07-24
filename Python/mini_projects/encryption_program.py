import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# key = chars.copy()
# random.shuffle(key)
key = ['m', '.', 'B', '1', '<', '#', 'T', '&', 'M', 'O', 'h', '{', 't', '_', ';', ':', '*', 'R', 'D', '8', '\\', '$', 'x', 'Z', 'w', '/', 'U', 'f', '6', '+', 'o', 'u', 'Q', '(', 's', '>', 'n', '5', 'z', '[', 'k', '0', 'b', ')', 'V', '}', 'a', 'i', 'j', 'r', '-', '2', '@', ']', 'e', '7', '`', ',', 'g', 'H', '3', '~', '^', 'K', 'v', 'N', 'Y', 'F', 'L', 'E', 'y', 'q', 'G', '%', 'W', '|', '?', '!', 'c', 'S', 'p', 'P', '=', 'X', "'", '"', ' ', '4', 'd', '9', 'I', 'A', 'l', 'C', 'J']

# print(f"chars : {chars}")
# print(f"key : {key}")

# Encrypt

plain_text = input("Enter a message: ")
cipher_text = ""
# print(plain_text)

for char in plain_text:
    index = chars.index(char)
    cipher_text += key[index]
    
print(f"Your message: {plain_text}")
print("================================")
print(f"Encrypted message: {cipher_text}")
print("================================")

# Decrypt

cipher_text = input("Enter message to Decrypt: ")
plain_text = ""
# print(plain_text)

for char in cipher_text:
    index = key.index(char)
    plain_text += chars[index]
    
print(f"Your message: {cipher_text}")
print("================================")
print(f"decrypted message: {plain_text}")
print("================================")