N=input()
M=[int(m) for m in N]
M.sort(reverse=True)
K=[str(o) for o in M]
print("".join(K))
