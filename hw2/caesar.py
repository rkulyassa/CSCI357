def caesar_encrypt(plaintext: str, shift: int) -> str:
    ciphertext = ""

    for char in plaintext:
        ordinal = ord(char)
        if 65 <= ordinal <= 90: # letter is capital (65-90)
            new_ordinal = (ordinal + shift - 65) % 26 + 65
            new_char = chr(new_ordinal)
        elif 97 <= ordinal <= 122: # letter is lowercase (97-122)
            new_ordinal = (ordinal + shift - 97) % 26 + 97
            new_char = chr(new_ordinal)
        else: # not a letter, don't shift
            new_char = char

        ciphertext += new_char
    
    return ciphertext

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    plaintext = ""

    for char in ciphertext:
        ordinal = ord(char)
        if 65 <= ordinal <= 90: # letter is capital (65-90)
            new_ordinal = (ordinal - shift - 65) % 26 + 65
            new_char = chr(new_ordinal)
        elif 97 <= ordinal <= 122: # letter is lowercase (97-122)
            new_ordinal = (ordinal - shift - 97) % 26 + 97
            new_char = chr(new_ordinal)
        else: # not a letter, don't shift
            new_char = char

        plaintext += new_char
    
    return plaintext

# Test case #1: full name with shift value 3
encrypted_name = caesar_encrypt("Ryan Kulyassa", 3)
print(encrypted_name) # Ubdq Nxobdvvd
descrypted_name = caesar_decrypt(encrypted_name, 3)
print(descrypted_name) # Ryan Kulyassa

# Test case #2: full name with shift value 20
encrypted_name = caesar_encrypt("Ryan Kulyassa", 20)
print(encrypted_name) # Lsuh Eofsummu
descrypted_name = caesar_decrypt(encrypted_name, 20)
print(descrypted_name) # Ryan Kulyassa