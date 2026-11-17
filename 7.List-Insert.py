# variable.insert(index,value): use , if you want add any other value in your list at any specific position(index).
list = ["mob","tom","ten","harry",65,12.444,True,False]
print(f"\nyour list: {list}")

#list.insert(5,"marsh") OR list.insert(-3,"marsh")  <-- this will not replace your list[5]-value
#if you want replace any value as, list[4]=65 -->  list[4]=60

list.insert(-3,"marsh")
print(f'\nAfter list.insert(5,"marsh") OR list.insert(-3,"marsh")')
print(f"\nYour updated list: {list}")
