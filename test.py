one = "hallo"
two = "hallohallo"
three = "hallohallohallo"

list1 = list()
list2 = list() 

list1.append(one)
list1.append(two)
list1.append(three)
list2.append(one)
list2.append(two)
list2.append(three)
print("List1: ", list1) 
print("List2: ", list2) 

del two 
print("List1: ", list1) 
print("List2: ", list2) 
print(two)