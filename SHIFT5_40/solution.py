# coding: utf-8

enc = "kqfl€6xdnydxynqqdy55djfx~D,"
flag = ""
for char in enc:
    flag += chr(ord(char)-5)

print flag

# Remove invalid characters, and add the last }
# flag{1s_it_still_t00_easy?}
