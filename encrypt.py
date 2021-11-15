name = "익명"
print(bin(ord(name[0]))[2:].zfill(16) + bin(ord(name[1]))[2:].zfill(16))
