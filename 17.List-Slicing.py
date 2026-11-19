#Slicing is just like range
list = [12,7,15,18,3,22,5,15,5,6,3,19,21]
print(f"\n1. if we want to print any slected index we print as print([index]).\nas, print(list[5])\nYour 5th index value:{list[5]}\n")

print(f"\n\nThink, What if we want to print range of value via index from a list ?\n\n")

print(f"\n2. We use list[start:end],where start = starting index from list and end = specified range's last index as, print(list[0:12])\nYour range list:{list[0:len(list)]}\n")

print(f"\n3. blank after ':' as, list[4:] cause end = last index\nYour '4:' list:{list[4:]}")

print(f"\n3. blank before ':' as, list[:8] cause start = first index\nYour ':8' list:{list[:8]}")

print(f"\n4. Also, is leave blank both before ':' and after ':' cause print whole range of list as, list[:]\nYour ':' list:{list[:]}")

print(f"\n5. we can also reverse a list as,list[len(list)::-1]\nYour revrsed list:{list[len(list)::-1]}") #reverse list
