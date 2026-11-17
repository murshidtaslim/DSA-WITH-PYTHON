#variable.clear(): use for delete entire list
list = ["harry","candella","mash","avion"]
print(f"\nYour list: {list}\nYour list id: {id(list)}")

print(f"\n# list = [] <-- Also remove entire list, But we use inbuilt function")
print(f"\n# list.clear()")
list.clear()

print(f"\nYour Empty list: {list}")

print(f"\nDifference B/W list=[] & list.clear()\nif you use list=[] then, computer makes new list at other id.\nBut if we use list.clear() then, computer properly delete list and id will remain same")
print(f"\nyour list id after list.clear(): {id(list)}")
list = []
print(f"\nAfter using list=[]\nYour list id: {id(list)}\n\nThis shows you are not delete list, but create blank new one.")
