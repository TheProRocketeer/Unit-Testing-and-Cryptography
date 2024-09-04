# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encode(text, n):
    new_str = ""
    for i in range(len(text)):
        index = alpha.index(i)
        if not (index + n > len(alpha)):
            new_str += alpha[index + n]
        else:
            new_str += alpha[(index + n) - len(alpha)]
    return new_str


def caesar_decode(text, n):
    new_str = ""
    for i in range(len(text)):
        index = alpha.index(i)
        if not (index - n < 0):
            new_str += alpha[index - n]
        else:
            new_str += alpha[(index - n) + len(alpha)]
    return new_str


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
