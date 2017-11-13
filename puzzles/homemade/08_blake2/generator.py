# TITLE: blake generator file:
# AUTHOR: Chalmer Lowe
# TODO:

# IMPORTS ==============================================
from random import randint, sample, shuffle
from hashlib import blake2b

# generate a word file
#     one word for line
#     1000

def gen_word_list(num=2000, keyword=None, out_location=None):
    '''Creates a list of words composed of two smaller words and a
    random number.
    '''

    with open('../data/1138090f.fic') as fin, open(out_location, 'w') as fout:
        words = [word.strip() for word in fin.readlines() if len(word) < 9]
        words = sample(words, num)
        pairs = zip(words[::2], words[1::2])

        outputs = []
        for pair in pairs:
            num = str(randint(1, 42))
            outputs.append(''.join(pair) + num + '\n')

        if keyword:
            outputs.append(str(keyword) + '\n')
            print('added malware')

        shuffle(outputs)
        for output in outputs:
            fout.write(output)

    return 'malwareministry13', outputs

# These words are used by the students...
# ... they read in these words...
output, outputs = gen_word_list(num=1998, keyword='malwareministry13', out_location='../data/real_words.txt')
print('The word:', output)

# These words are used to create the fake hashes...
# ... these words create a batch of fake hashes with ONE real hash...
junk, outputs = gen_word_list(num=1998, keyword='malwareministry13',
                              out_location='../data/fake_words.txt')


outputs = [output.strip() for output in outputs]
# generate a hash file
#     one hash per line
#     1000

with open('hashes.txt', 'w') as hashout:
    print('starting hashes...')
    for word in outputs:
        digest = blake2b(word.encode(),
                        digest_size=30,       # size of digest in bytes
                        key=b'biochemical',         # up to 64 bytes
                        salt=b'impractical',         # up to 16 bytes
                        person=b'juxtaposing',       # up to 16 bytes
                        ).hexdigest()
        if word == output:
            print(word, digest)
        hashout.write(digest + '\n')

# hashlib.blake2b(word.encode(), digest_size=30, key=b'mykey', salt=b'dead', person=b'beef').hexdigest()

# The following code is commented out to prevent inadvertant overwrites of
#     the files listed below.

'''
possibles = [word.strip() for word in open('../data/1138090f.fic').readlines()
                 if len(word) > 11]
'''

'''
# generate content for a key file
#     one key per line
#     20
print('keys:', '-' * 40)
for item in possibles[::501][:20]:
    print(item)

# generate a salt file
#     salts in a csv
#     20
print('salts:', '-' * 40)
for item in possibles[::500][:20]:
    print(item)

# generate a personalization file
#     one personalization string per line
#     20
print('personalizations:', '-' * 40)
for item in possibles[::504][:20]:
    print(item)
'''
