# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encode(text, n):
    new_str = ""
    for let in text:
        if let.lower() not in alpha.lower():
            new_str += let
        else:
            index = alpha.lower().index(let.lower())
            if not (index + n > len(alpha)):
                if let.isupper():
                    new_str += alpha[index + n]
                else:
                    new_str += alpha[index + n].lower()
            else:
                if let.isupper():
                    new_str += alpha[(index + n) - len(alpha)]
                else:
                    new_str += alpha[(index + n) - len(alpha)].lower()
    return new_str


def caesar_decode(text, n):
    new_str = ""
    for let in text:
        if let.lower() not in alpha.lower():
            new_str += let
        else:
            index = alpha.lower().index(let.lower())
            if not (index - n < 0):
                if let.isupper():
                    new_str += alpha[index - n]
                else:
                    new_str += alpha[index - n].lower()
            else:
                if let.isupper():
                    new_str += alpha[(index - n) + len(alpha)]
                else:
                    new_str += alpha[(index - n) + len(alpha)].lower()
    return new_str

test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
