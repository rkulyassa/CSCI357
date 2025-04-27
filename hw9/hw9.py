import hashlib
first_name = b"Ryan"

trial_224_0 = hashlib.sha3_224(first_name).hexdigest()
trial_256_0 = hashlib.sha3_256(first_name).hexdigest()
trial_384_0 = hashlib.sha3_384(first_name).hexdigest()
trial_512_0 = hashlib.sha3_512(first_name).hexdigest()

last_name = b"Kulyassa"
trial_224_1 = hashlib.sha3_224(first_name + last_name).hexdigest()
trial_256_1 = hashlib.sha3_256(first_name + last_name).hexdigest()
trial_384_1 = hashlib.sha3_384(first_name + last_name).hexdigest()
trial_512_1 = hashlib.sha3_512(first_name + last_name).hexdigest()


print(trial_224_0)
print(trial_224_1)

matches = []
for i in range(len(trial_224_0)):
    if trial_224_0[i] == trial_224_1[i]:
        matches.append(i)

print(f"Matches for SHA3-244: {len(matches)} (positions {', '.join(str(m) for m in matches)})")


print()
print(trial_256_0)
print(trial_256_1)

matches = []
for i in range(len(trial_256_0)):
    if trial_256_0[i] == trial_256_1[i]:
        matches.append(i)

print(f"Matches for SHA3-256: {len(matches)} (positions {', '.join(str(m) for m in matches)})")


print()
print(trial_384_0)
print(trial_384_1)

matches = []
for i in range(len(trial_384_0)):
    if trial_384_0[i] == trial_384_1[i]:
        matches.append(i)

print(f"Matches for SHA3-384: {len(matches)} (positions {', '.join(str(m) for m in matches)})")


print()
print(trial_512_0)
print(trial_512_1)

matches = []
for i in range(len(trial_512_0)):
    if trial_512_0[i] == trial_512_1[i]:
        matches.append(i)

print(f"Matches for SHA3-512: {len(matches)} (positions {', '.join(str(m) for m in matches)})")