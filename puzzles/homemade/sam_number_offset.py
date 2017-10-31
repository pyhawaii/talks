# The file number_offset.txt contains a series of letters, numbers, punctuation
#     and spaces. Every NUMBER identifies the location of a CHARACTER that is
#     important. To find the right characters, locate each number and then count
#     forward by that many characters to find the character of interest. For
#     example, if given the string:

#     abcdefg5hijklmnop3qrstuvw
#            |    ^    |  ^
#             12345     123

#     the fifth character after the 5 is an 'l' and the third character after
#     the 3 is an 's'.
# Save all the CHARACTERS to spell out a phrase.
# Go find it.

import re


text = open('number_offset.txt').read()

number_indices = [ m.start(0) for m in re.finditer('[0-9]', text)]

character_indices = [n + int(text[n]) for n in number_indices]

solution = ''.join([text[i] for i in character_indices if i < len(text)])

print(solution)
