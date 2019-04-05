from itertools import permutations
perms = [''.join(p) for p in permutations(['0','1','2','3','4','5','6','7','8','9'])]
print perms[999999]
