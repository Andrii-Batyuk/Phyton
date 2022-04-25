p = 1
q = 1

a = not (p and q) == (not p) or (not q)
b = not (p or q) == (not p) or (not q)
print(a , b)
