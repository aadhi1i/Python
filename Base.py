a = 3 + 4j
b = 1 + 2j

sum = a + b
product = a * b

print("Sum of a and b:", sum)
print("Product of a and b:", product)

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.extend([7, 8, 9])

print(numbers[::-1])

list = [10, 20.5, 3 + 4j, "Python"]
list.append("Programming")
print(list)
list.extend([100, 200])

print(list[-1])

text = "Python Programming"
new_text = text[:6] + text[-11:]

print(new_text)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
list3 = list1 + [7, 8, 9]

print(list3[2])


l=["python","swift","ruby"]
l[2]="c"
print(l)

pn=[2,4,6,7]
re=pn.pop(2)
print("removed element",re)
print("update list",pn)

l=["python","ruby","c","java","rust"]
del l[1]
print(l)
del l[-1]
print(l)
del l[0:2]
print(l)

l=["python","ruby","c","java","rust"]
l.remove("c")
print(l)

reverselist
pn=[2,3,5,7]
pn.reverse()
print("reversed list",pn)

li=[1,3,4,6,8,9]
for i in li:
    print(i)



li=[11,13,14,16,18,19]
l=li*2
print(l)

li=[12,31,42,61]
lo=[3,5,6,7,8]
l=li+lo
print(l)

li=[1,3,4,6,8,9]
a=len(li)
print(a)

li=["john","kate","david","james"]
for i in li:
    print(i)

li=[100,300,440,620,810,900]
print(500 in li)
print(100 in li)

li=[1,3,4,6,8,9]
print(max(li))

li=[1,3,4,6,8,9]
print(min(li))

li=[1,3,4,6,8,9]
lo=[3,4,6,5]
m=set(li).intersection(lo)
print(m)

li=[1,3,4,6,8,9]
lo=[1,8,4,6,5,9]
m=set(li) & set(lo)
print(m)

