import random


def generate_random_key(size: int) -> bytes:
    key = [str(random.choice([0, 1])) for _ in range(size)]
    return "".join(key).encode("utf-8")


def bitwise_xor(binary_string1, binary_string2) -> bytes:
    return bytes(a ^ b for a, b in zip(binary_string1, binary_string2))


# Convert your first name into its binary representation using UTF-8 encoding.
first_name = "Ryan".encode("utf-8")

# Generate a random key with the same size as the binary representation of your
# first name using the generate_random_key() function you created in Part 1.
key = generate_random_key(len(first_name))

# Encrypt your first name's binary representation using the generated key and
# the bitwise_xor() function you created in Part 2.
encrypted_name = bitwise_xor(first_name, key)

# Decrypt the resulting ciphertext using the same key and the bitwise_xor() function.
decrypted_name = bitwise_xor(encrypted_name, key)

print("Name:", first_name)
print("Key:", key)
print("Ciphertext:", encrypted_name)
print("Decrypted binary:", decrypted_name)
print("Decrypted text:", decrypted_name.decode())
