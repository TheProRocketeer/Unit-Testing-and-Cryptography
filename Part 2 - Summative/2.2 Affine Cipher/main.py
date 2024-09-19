import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    new_str = ""
    newer_str = ""
    for let in text:
        if let.lower() not in alpha.lower():
            new_str += let
        else:
            index_b = alpha.lower().index(let.lower())
            index_a = index_b * (a % len(alpha)) % len(alpha)
            new_str += alpha[index_a]
    for let in new_str:
        index_c = alpha.lower().index(let.lower())
        newer_str += alpha[(index_c + b) % len(alpha)]
    return newer_str

def affine_decode(text, a, b):
    new_str = ""
    newer_str = ""
    for let in text:
        if let.lower() not in alpha.lower():
            new_str += let
        else:
            index_c = alpha.lower().index(let.lower())
            new_str += alpha[(index_c - b) % len(alpha)]
    for let in new_str:
        index_b = alpha.lower().index(let.lower())
        index_a = index_b * (mod_inverse(a, len(alpha))) % len(alpha)
        newer_str += alpha[index_a]
    return newer_str

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    new_num = 0
    for i in range(len(ngram)):
        new_num += alpha.lower().index(ngram[i].lower()) * (26**i)
    return new_num

def convert_to_text(num, n):
    new_str = ""
    new_num = num
    for i in range(n - 1):
        new_num = new_num / 26
        new_str += alpha[int(new_num % 26)]
    return new_str

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    return ''

def affine_n_decode(text, n, a, b):
    return ''

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!