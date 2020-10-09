'''
This module explores the use of a caesar cipher, a monoalphabetic substitution cipher, built in Python.
The excercise uses functions, modulo arithmetic, loops and list methods
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Helper function to wrap around the alphabet
def alphabet_wrapper(x, offset, cipher_mode):
    alphabet_length = len(alphabet)

    # Set wrap mode (which direction we are moving depending on encrypting vs decrypting)
    if cipher_mode == 'e':
        # Encryption Mode /  Shift to the left
        if alphabet.index(x) - offset >= 0:
            return alphabet[alphabet.index(x) - offset]
        else:
            wrap_value_left = offset % alphabet_length
            if alphabet.index(x) - wrap_value_left >= 0:
                return alphabet[alphabet.index(x) - wrap_value_left]
            return alphabet[alphabet.index(x) - wrap_value_left]
    else:
        # Decryption Mode / Shift to the right
        if offset + alphabet.index(x) <= alphabet_length - 1:
            return alphabet[alphabet.index(x) + offset]
        else:
            wrap_value_right = (alphabet.index(x) + offset) % alphabet_length
            return alphabet[wrap_value_right]

def cipher(msg, offset, mode='e'):
    lowercase = msg.lower()
    message = ''
    for i in lowercase:
        if i in alphabet:
            value = alphabet_wrapper(i, offset, mode)
            message += value
        else:
            message += i
    print(message)

# Test / Debug Statements
cipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 3, 'e')
cipher("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD", 3, 'd')

''' This statement below is to brute force test up to 100 possible offset values '''
# for i in range(100):
#     cipher("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD", i, 'd')
#     print(i)