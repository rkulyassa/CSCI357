# Crypto HW - submit the python code and a pdf summarizing what the code does.

def caesar_encrypt(plaintext: str, shift: int) -> str:
    ciphertext = ""

    for char in plaintext:
        ciphertext += chr(ord(char) + (shift % 26))
    
    return ciphertext

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    plaintext = ""

    for char in ciphertext:
        plaintext += chr(ord(char) - (shift % 26))
    
    return plaintext

encrypted_name = caesar_encrypt("Ryan Kulyassa", 3)
print(caesar_decrypt(encrypted_name, 3))

encrypted_name = caesar_encrypt("Ryan Kulyassa", 20)
print(caesar_decrypt(encrypted_name, 20))