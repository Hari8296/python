Name :- Hari singh r 
Batch id :-  DSWDMCOD 25082022 B

import pandas as pn
1

#a
list1= pn.DataFrame({"X1":[1,2,3],"X2":[4,8,12],})
list2= pn.DataFrame({"X1":[4,5,6],"X2":[14,16,18],})

Concatenating = pn.concat([list1,list2],axis=1)
print(Concatenating)

#b
string = "ram is good player"
substring="o"
count=string.count(substring)
print(count)

#c
a=[1,2,3,4,5,6,7,8,9,10]
a.reverse()
print(a)


2
# a find a common elements

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {5,6,7,8,9,10,11,12,13,14,15}

list = set1.intersection(set2)
print(list)

# b find the elements are not common 

list = set1.symmetric_difference(set2)
print(list) 

# c removing element 7

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [5,6,7,8,9,10,11,12,13,14,15]

print(list1.pop(6))
print(list2.pop(2))
print(list1,list2)

3
# a 

dict1={'karnataka':52,'tamil nadu':65,'kerala':89,'himachal pradesh':10,'bihar':88}
print(dict1)
print(dict1['karnataka'])
print(dict1['tamil nadu'])
print(dict1['kerala'])
print(dict1['himachal pradesh'])
print(dict1['bihar'])

#b
dict1['chennai']=85
print(dict1)

