""" Encoded Messages
Description

Krasi is tasked to invent a program for validating messages. He creates a program which from every message that is received would create a corresponding sequence of encoded characters. That way he would be able to verify the authenticity of the message.

The encoding algorithm will work as described below:

    If the word is equal to or longer than 3 characters, the first and the last characters of the word are encoded in a way where we need to provide the next characters in the ASCII table. The part of the word without the first and the last characters are represented as the length of those symbols.
    Numbers equal to or longer than 3 digits are also encoded.
    If the word / number consists of less than 3 characters it does not change.
    White space are passed through as they are.

Example:
Input

1000000 dollar

Output

251 e4s

Explanation:
The first sequence of characters to encode is 1000000. It is equal to or longer than 3 characters hence we need to encode it. We substitute the first character 1 with the next character in the ASCII table which is 2, then substitute the last character 0 with 1 and inbetween we add the length of the rest: 5 so we end up with 251. The second sequence is also equal to or longer than 3 characters. Here d is replaced by e. r is replaced by s and the characters in the middle replaced by their length 4.
Input

    The message that the program needs to encode.

Output

    The encoded message.

Constraints

    Each word will contain only numbers, lowercase or uppercase letters from the English alphabet.

Sample tests
Input

Very secret message to communicate

Output

W2z t4u n5f to d9f

Input

The biggest secret in the world

Output

U1f c5u t4u in u1f x3e
"""

message = input().split()
edited_message = []

for current_element in message:
    if len(current_element) >= 3:
        current_el_as_list = [str(x) for x in current_element]
        edited_el = []

        edited_el.append(chr(ord(current_el_as_list[0]) + 1))
        edited_el.append(len(current_el_as_list[1:-1]))
        edited_el.append(chr(ord(current_el_as_list[- 1]) + 1))
        edited_message.append("".join([str(x) for x in edited_el]))
    else:
        edited_message.append(current_element)

print(' '.join(edited_message))
