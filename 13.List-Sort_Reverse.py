#list.sort() use for sorting list
#list.reverse() use for reverse list
#list.sort(reverse=True) also use for reverse with sorting
list = [2,5,2,5,6,457,47,3,6,42,2,34,34,5,4,433,543,346,54]
print(f"\nYour list --> {list}")
list.reverse()
print(f"\nAfter list.reverse() --> {list}")
list.sort(reverse=True)
print(f"\nAfter list.sort(reverse=True) --> {list}")
list.sort()
print(f"\nAfter list.sort() --> {list}")
