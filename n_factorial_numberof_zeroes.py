N = 45321

def get_tail_nzeroes(n):
    n_five = 0
    while n % 5 == 0:
        n_five += 1
        n = n / 5
    return n_five

five = 0
while N > 1:
    this_five = get_tail_nzeroes(N)
    five += this_five
    N -= 1

print five
