def vigenere_encrypt(plaintext: str, key: str) -> str:
    ciphertext = ""

    for i in range(len(plaintext)):
        plaintext_char = plaintext[i]
        key_char = key[i % len(key)]

        if plaintext_char.isalpha():
            plaintext_char_index = ord(plaintext_char) - 65 if plaintext_char.isupper() else ord(plaintext_char) - 97
            if key_char.isalpha():
                key_char_index = ord(key_char) - 65 if key_char.isupper() else ord(key_char) - 97
            else:
                key_char_index = ord(key_char)
            ciphertext_char_index = (plaintext_char_index + key_char_index) % 26
            ciphertext_char_index += 65 if plaintext_char.isupper() else 97
            ciphertext += chr(ciphertext_char_index)
        else:
            ciphertext += plaintext_char
    
    return ciphertext

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    plaintext = ""

    for i in range(len(ciphertext)):
        ciphertext_char = ciphertext[i]
        key_char = key[i % len(key)]

        if ciphertext_char.isalpha():
            ciphertext_char_index = ord(ciphertext_char) - 65 if ciphertext_char.isupper() else ord(ciphertext_char) - 97
            if key_char.isalpha():
                key_char_index = ord(key_char) - 65 if key_char.isupper() else ord(key_char) - 97
            else:
                key_char_index = ord(key_char)
            plaintext_char_index = (ciphertext_char_index - key_char_index) % 26
            plaintext_char_index += 65 if ciphertext_char.isupper() else 97
            plaintext += chr(plaintext_char_index)
        else:
            plaintext += ciphertext_char
    
    return plaintext

plaintext_name = "Ryan Kulyassa"
key = "CSCI357"
print("Original plaintext:", plaintext_name)
encrypted_name = vigenere_encrypt(plaintext_name, key)
print("Encrypted ciphertext:", encrypted_name)
decrypted_name = vigenere_decrypt(encrypted_name, key)
print("Decrypted plaintext:", decrypted_name)
