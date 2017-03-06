S = "fdxnfxfnxdfsajpoij4oijfodisu98uoifjjjjjjjjjjjjjjjjdspoayufr32vyht432y9f8d9p38nv983nvdsz98yu73nvoifdp9831ndsa02"

S1 = '?'

for c in S:
    S1 += '#'
    S1 += c

S1 += '#$'

RL = [0 for i in S1]

max_right = 0
pos = 0

max_len = 0

for idx, c1 in enumerate(S1):
    if idx < max_right:
        RL[idx] = min(max_right - idx, RL[2*pos-idx])
        t = idx - RL[idx]
        while t < idx + RL[idx]:
            print S1[t],
            t += 1
    else:
        print '<', S1[idx]
        RL[idx] = 0
    print

    while S1[idx + RL[idx]] == S1[idx - RL[idx]]:
        RL[idx] += 1
        if idx + RL[idx] >= len(S1) - 1 or idx - RL[idx] <= 0:
            break

    pos = idx

    if max_right < idx + RL[idx]:
        max_right = idx + RL[idx]

    if max_len < RL[idx]:
        max_len = RL[idx]

print max_len - 1
