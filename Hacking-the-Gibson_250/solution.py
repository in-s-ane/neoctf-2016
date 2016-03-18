enc = "\v\v+(.M"
flag = ""
for char in enc:
    flag += chr(ord(char) ^ 108)

print flag

# Disassembling the executable revealed that some sort of string was being xor'd by 108
# and that was being compared to the user's input. We can xor the encrypted string back
# to get the flag, since xor(xor(m, n), n) = m

# ggGDB!
