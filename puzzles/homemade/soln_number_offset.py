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


text = list(open('number_offset.txt').read())

counter = 0
increment = -1
output = []

for index, char in enumerate(text, 1):
    if char.isdigit():
        increment = int(char)
        # reset the counter
        counter = -1

    # increment the counter to enable the identification of the
    #     character of interest
    counter += 1

    # if the counter becomes equal to the increment
    # reset both variables and save off the character
    if counter == increment:
        counter = 0
        increment = -1
        output.append(char)

print(''.join(output))
