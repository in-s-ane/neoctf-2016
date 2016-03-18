import string

alphabet = string.printable

enc = "nukr{JAxhUWVEkdJp}"

flag = "flag{"
k1 = 8
k2 = 10

def encrypt(string, k1, k2):
    enc = ""
    for char in string:
        if char in "{}":
            enc += char
            continue
        if ord(char)%2 == 0:
            enc += chr(ord(char)+k1)
            k1 += 1
        else:
            enc += chr(ord(char)+k2)
            k2 += 1
    return enc

for x in range(len(enc)):
    for letter in alphabet:
        candidate = flag + letter
        if encrypt(candidate, k1, k2) == enc[:len(candidate)]:
            flag = candidate
            break
print flag

# for letter in alphabet:
#     candidate = "flag{@5k" + letter
#     if encrypt(candidate, k1, k2) == "nukr{JAxh":
#         flag = candidate
#         print letter
#         print candidate
#         break

# print flag
