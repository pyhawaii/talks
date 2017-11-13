# TITLE: blake generator file:
# AUTHOR: Chalmer Lowe

# IMPORTS ==============================================
from random import randint, sample, shuffle
from hashlib import blake2b
import itertools

# Read in all the terms in the various files:
#     keys, salts, personalizations, hashes and words...


# KEYS:
with open('keys.txt') as keys_in:
    keys = []
    for line in keys_in:
        keys.append(line.strip().split()[1])

# SALTS:
with open('salt.csv') as salts_in:
    salts = salts_in.readline().strip().split(';')

# PERSONALIZATIONS:
with open('personalization.txt') as pers_in:
    pers = [term.strip() for term in pers_in.readlines()]

# HASHES:
with open('hashes.txt') as hashin:
    hashes = {h.strip() for h in hashin.readlines()}

# WORDS:
with open('real_words.txt') as wordsin:
    words = [w.strip() for w in wordsin.readlines()]


# Produce all the products of the four main inputs to the hashing algorithm
#     words, keys, salts, personalizations

combos = [words, keys, salts, pers]
products = list(itertools.product(*combos))

for item in products:
    word, key, salt, pers = [term.encode() for term in item]
    digest = blake2b(word,
                     digest_size=30,       # size of digest in bytes
                     key=key,         # up to 64 bytes
                     salt=salt,         # up to 16 bytes
                     person=pers,       # up to 16 bytes
                     ).hexdigest()

    if digest in hashes:
        print('found it:', digest, word, key, salt, pers)
