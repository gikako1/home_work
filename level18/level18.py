list=[1,2,2,4,5,6,7]

#copy
x=list.copy()
print(x)

#Append
list.append(8)
print(list)

#pop
list.pop(6)
print(list)

#count
x=list.count(2)
print(x)

#extend
extender=[0,9,8]
list.extend(extender)
print(list)

#index
x=list.index(6)
print(x)

#insert
list.insert(1,19)
print(list)

#remove
list.remove(19)
print(list)

#reverse
list.reverse()
print(list)
list.reverse()
print(list)

#sort
list.sort(reverse=True)
print(list)
list.sort(reverse=False)
print(list)

#clear
list.clear()
print(list)

