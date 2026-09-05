print("parity - last bit = 0 even, last bite =  odd")
for n in [2,3,4,5,8,9]:
  if n & 1:
    print(" ", n, "-> odd")
  else:
    print(" ", n, "-> even")
