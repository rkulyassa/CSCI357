import random

# Generate a random integer, n, between 5 and 10 (inclusive).
# This integer, n, will represent the block size in bits for your simple block cipher.
n = random.randint(5, 10)

# Create a mapping (your "key") that defines a substitution for each possible n-bit block.
patterns = []
for i in range(1 << n):
    pattern = bin(i)[2:]
    pattern = "0" * (n - len(pattern)) + pattern
    patterns.append(pattern)

key = {}
used = patterns.copy()
for pattern in patterns:
    key[pattern] = used.pop(random.randint(0, len(used)-1))

# Convert the letters of your last name into their ASCII binary representations.
# Concatenate the binary representations of the letters in your last name.
last_name = "Kulyassa"
bin_last_name = ""
for char in last_name:
    bin_char = bin(ord(char))[2:]
    bin_last_name += bin_char

# Pad the resulting bit string with leading zeros, if necessary,
# to ensure that the total length of the bit string is a multiple of n (your block size).
while len(bin_last_name) % n != 0:
    bin_last_name += "0"

print(key)
print(bin_last_name)