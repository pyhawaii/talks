# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:07:34 2017

@author: nathaniel
"""

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

# Using for loop
def attempt1(data):
    answer = []
    for i, char in enumerate(data):
        # use try to avoid out of index errors
        try:
            # if the character is a digit
            if char.isdigit():
                # add the specified character at the index plus char to the answer
                answer.append(data[int(char)+i])
        except IndexError:
            # For clarity on where index errors occur
            #print(f'Out of index error at index: {i + int(data[i])}\n\n')
            pass # Ignores out of index character
        except:
            print('There was an unhandled exception') # unexpected
    
    # Join the list of characters into a string
    answer = ''.join(answer)
    return answer

# List comprehension version of attempt1
def attempt2(data):
    answer = []
    # Add the hidden characters at the index plus char to the answer
    try: 
        [answer.append(data[int(char)+i]) for i, char in enumerate(data) if char.isdigit()]
    except: 
        pass # Ignores out of index character
    return ''.join(answer)

if __name__ == '__main__':
    with open('number_offset.txt') as f:
        data = f.read()
    print(f'Attempt1: "{attempt1(data)}"')
    print(f'Attempt2: "{attempt2(data)}"')
    