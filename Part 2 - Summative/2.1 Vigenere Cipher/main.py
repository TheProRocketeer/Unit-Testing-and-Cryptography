# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  new_str = ""
  i = -1
  for let in text:
    i += 1
    if let.lower() not in alpha.lower():
      new_str += let
    else:
      index_a = alpha.lower().index(let.lower())
      index_b = alpha.lower().index(keyword[(i % len(keyword))].lower())
      if index_a + index_b > len(alpha):
        if let.isupper():
          new_str += alpha[index_a + index_b - 26]
        else:
          new_str += alpha[index_a + index_b - 26].lower()
      else:
        if let.isupper():
          new_str += alpha[index_a + index_b]
        else:
          new_str += alpha[index_a + index_b].lower()
  return new_str


def vig_decode(text, keyword):
  new_str = ""
  i = -1
  for let in text:
    i += 1
    if let.lower() not in alpha.lower():
      new_str += let
    else:
      index_a = alpha.lower().index(let.lower())
      index_b = alpha.lower().index(keyword[(i % len(keyword))].lower())
      if index_a + index_b < len(alpha):
        if let.isupper():
          new_str += alpha[index_a - index_b + 26]
        else:
          new_str += alpha[index_a - index_b + 26].lower()
      else:
        if let.isupper():
          new_str += alpha[index_a - index_b]
        else:
          new_str += alpha[index_a - index_b].lower()
  return new_str


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!