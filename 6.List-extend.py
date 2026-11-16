# variable.extend():use for assign values of another list in first list as, list2-->list1
list1 = ["mob","bob","ten","marsh",65,848234586/2,55.833]
list2 = [1,2,3,4]

# list1.append(list2) <-- this cause, create another list inside your list1.

"""for i in list2:
    list1.append(i)""" # <-- this loop perform well. But we use inbuilt function

print(f"\nlist1: {list1}")
print(f"\nlist2: {list2}")
# list1.extend(list2)
print("\nlist1.extend(list2)")
list1.extend(list2)

print(f"\nMerged list1+list2: {list1}")
