#variable.copy() use for copy list data to another list
list = [1,2,3]

list1 = list #deep copy
print(f"list --> {list}")
print(f"After --> list1 = list")
print(f"list1 --> {list1}")

list.append(4)
print(f"\nlist.append(4) --> this cause only add 4 at last of list,\nBut it not happened because list & list1 pointing same reference,\nYou see both have same ID\n\nYour list --> {list} ID:{id(list)}\nYour list1 --> {list1} ID:{id(list1)}")

list2 = list.copy() #swallo copy
list.append(5)
print(f"\nAfter --> list2 = list.copy()")
print(f"\nlist.append(5) --> this cause add 5 at last of list not list2,\nID of list and list 2 is changed\n\nYour Updated-list --> {list} ID:{id(list)}\nYour list2 --> {list2} ID:{id(list2)}")
