flag = "f"
enc = "1101100 10121 1213 443 121 141 103 115 66 5a 97 54 83 85".split()
for x in range(len(enc)):
    flag += chr(int(enc[x], x+2))

print flag

# flag{1NC_BAsEs}
