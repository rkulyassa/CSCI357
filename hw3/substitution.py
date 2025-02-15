import random
import string

def encrypt_message(plaintext: str, key: str) -> str:
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            index = string.ascii_uppercase.index(char.upper())
            new_char = key[index]
            ciphertext += new_char if char.istitle() else new_char.lower()
        else:
            ciphertext += char
    
    return ciphertext

def decrypt_message(ciphertext: str, key: str) -> str:
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            index = key.index(char.upper())
            new_char = string.ascii_uppercase[index]
            plaintext += new_char if char.istitle() else new_char.lower()
        else:
            plaintext += char
    
    return plaintext

def generate_random_key() -> str:
    letters_list = list(string.ascii_uppercase)
    random.shuffle(letters_list)
    key = "".join(letters_list)
    return key

key = generate_random_key()
print("Key:", key)

plaintext_name = "Ryan Kulyassa"
print("Original plaintext:", plaintext_name)
encrypted_name = encrypt_message(plaintext_name, key)
print("Encrypted ciphertext:", encrypted_name)
descrypted_name = decrypt_message(encrypted_name, key)
print("Decrypted plaintext:", descrypted_name) # Ryan Kulyassa