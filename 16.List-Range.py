#variable(range(start,end)) or variable(range(start,end,step condit.)) used for print list of ani perticular range of numbers as shown below
#when use range function, we see that list start with "start" and with "end-1"

print(f"\n1. \"print(range(1,10))\": In range we entered end = 10 ,But here list end = end-1\n")
print(f"Your list: {list(range(1,10))}\n")

print(f"\n2. \"print(range(20,1))\": Descending range is not work\n")
print(f"Your list: {list(range(20,1))}\n")

print(f"\n3. \"print(range(2,21,2))\": Here, we passing step condition after end, which is 2, it cause your range continuous skip by 2\n")
print(f"Your list: {list(range(2,21,2))}\n")

print(f"\n4. \"print(range(20,0,-2))\": Descending range also works if you pass a skipping step as -2\n")
print(f"Your list: {list(range(20,0,-2))}\n")
