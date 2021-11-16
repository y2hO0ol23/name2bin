#version4
name = "ㅁㄴㅇㄹ"
result = ""
for i in name:
    i = bin(ord(i))[2:]
    t = 0
    for j in range(1, len(i) - 1):
        x = int("".join(i[:j]),2)
        y = int("".join(i[j:]),2)
        t ^= x ^ y ^ x*y
    result += bin(t)[2:].zfill(16)

for i in range(1,len(result)):
    t = ""
    for j in range(i):
        t = result[j::i] + t
    result = t
result = int(result,2)

dec = 0
s = 1
while result > 0:
    if s == 1:
        dec ^= result & 0xffffffff
    else:
        dec ^= int(bin(result & 0xffffffff)[2:][-1::-1],2)
    s *= -1
    result = result >> 32
    
print(dec)
print(bin(dec)[2:].zfill(32))
print(hex(dec)[2:].zfill(8).upper())

#version3
"""
name = "익명"
temp = ""
for i in name:
    temp += bin(ord(i))[2:].zfill(16)
name = temp

result = 0
for i in range(1, len(name) - 1):
    x = int("".join(name[:i]),2)
    y = int("".join(name[i:]),2)
    result ^= x ^ y ^ x*y

dec = 0
while result > 0:
    dec ^= result & 0xffffffff
    result = result >> 32
print(bin(dec)[2:].zfill(32))
print(hex(dec)[2:].zfill(8).upper())
"""

#version 2
"""
name = "익명"
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
"""

#version 1
"""
name = "익명" #must be 2 character
print(bin(ord(name[0]))[2:].zfill(16) + bin(ord(name[1]))[2:].zfill(16))
"""
