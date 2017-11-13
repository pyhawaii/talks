# Hash puzzle
#
# You are presented a series of files and must use the contents to
#     identify the answer: a specific 'word' that was hashed using the
#     blake2b() hashing algorithm.

# WARNING: this puzzle is intended to be performed on a
#          64-bit machine... There is no guarantee that the hashing algorithm
#          will generate the same values on a 32-bit machine

# As an example, if given the following:
#     digest = 10
#     word =   b'pythonrocks07',
#     key =    b'guido',
#     salt =   b'pandas',
#     personalization = b'bokeh' the blake2b() function will produce
#     the following hash:
#
#     47dbf8bd8e4e860ee810 (a 10-byte hash)

# Your answer would be the word 'pythonrocks07'

# The files include:
#     WORDS:  real_words.txt, which contains multiple words, only one of which
#             produced a hash in the file hashes.txt
#     HASHES: hashes.txt, which has multiple hash hexdigests, only one of which
#             is associated with the a word from the WORDS file
#     KEYS:   keys.txt, which contains multiple possible keys, only one of
#             which was used in the production of the hash of interest
#     SALTS:  salt.csv, which contains multiple possible salts, only one of
#             which was used in the production of the hash of interest
#     PERSONALIZATIONS: personalization.txt, which contains multiple possible
#                       personalizations, only one of which was used in the
#                       production of the hash of interest
#
#
# NOTE: The word will be a combination of two shorter words and a number
# NOTE: To find the right word, you will have to derive the hexdigests
#       of each of the words, using all the possible combinations of
#       keys, salts, personalizations and match it against the hexdigests in the
#       hashes.txt file.
# NOTE: You will also need to determine the correct digest length
# NOTE: Be careful of the file formats and the file content ... they are
#       purposely diverse in structure and formatting

# Put your code here:
