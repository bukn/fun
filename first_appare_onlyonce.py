S = "fdsajpoij4oijfodisu98uoifjdspoayufr32vyht432y9f8d9p38nv983nvdsz98yu73nvoifdp9831ndsa02"
minascii = 0x21
maxascii = 0x7f

searchList = [[0,0]  for i in range(maxascii - minascii)]
i = 0
while i < len(S):
    tmpchar = S[i]
    idx = ord(tmpchar)-minascii
    if searchList[idx][0] == 0: #first time appare
        searchList[idx][1] = i
    searchList[idx][0] += 1
    i += 1


minidx = len(S)
for j,item in enumerate(searchList):
    if item[0] == 1:
        if item[1] < minidx:
            minidx = item[1]

print(minidx)
print(S[minidx])
