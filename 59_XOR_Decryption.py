'''
Created on Dec 4, 2023

Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42,
and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each
byte with a given value, taken from a secret key. The advantage with the XOR function is that
using the same encryption key on the cipher text, restores the plain text; for example,
65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key
is made up of random bytes. The user would keep the encrypted message and the encryption key
in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a
password as a key. If the password is shorter than the message, which is likely, the key is
repeated cyclically throughout the message. The balance for this method is using a sufficiently
long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the
encrypted ASCII codes, and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
'''
from datetime import datetime
from string import ascii_lowercase


if __name__ == '__main__':
    start = datetime.now()

    common_words = [
        'and',
        'the',
        'that',
        # 'have',
        # 'not'
    ]

    with open('0059_cipher.txt') as src:
        encrypted = src.read().split(',')
    encrypted = [int(x) for x in encrypted]

    # Char to Int --> a: 97, ..., z: 122

    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                pwd = [ord(x) for x in (a, b, c)]
                decrypted = [
                    pwd[i % 3] ^ x
                    for i, x in enumerate(encrypted)
                ]
                char_decrypted = [
                    chr(x) for x in decrypted
                ]
                decoded_msg = ''.join(char_decrypted)
                if all(word in decoded_msg for word in common_words):
                    print(decoded_msg)
                    print(sum(decrypted))

    end = datetime.now()
    print(f'\nruntime = {end - start}')
