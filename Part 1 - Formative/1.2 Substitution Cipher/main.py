# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    new_str = ""
    for let in text:
        index = alpha.lower().index(let.lower())
        if let.isupper():
            new_str += codebet[index]
        else:
            new_str += codebet[index].lower()
    return new_str


def sub_decode(text, codebet):
    new_str = ""
    for let in text:
        index = codebet.lower().index(let.lower())
        if let.isupper():
            new_str += alpha[index]
        else:
            new_str += alpha[index].lower()
    return new_str


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
