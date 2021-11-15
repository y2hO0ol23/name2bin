name = ""
if len(name) <= 3:
    name += "디코이름난독화"
if len(name) % 2 == 1:
    name += "디코이름난독화"

result = [0 for _ in range(32)]
for i in range(0,len(name),2):
    bindata = list(bin(ord(name[i]))[2:].zfill(16) + bin(ord(name[i+1]))[2:].zfill(16))
    for j in range(32):
        result[j] ^= int(bindata[j])

print("".join(map(str,result)))
