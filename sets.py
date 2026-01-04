# # Learning the sets and its some function
# # large amount of the can be stored in one variale
# # set is unordered

# a={10,20,30,40,50}
# print(a)
# for i in a :
#     print(i)

a={10,20,30,40,50,}
b={40,50,60,70,80}
c={10,20}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
# print(b.difference(a))
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(c.issubset(a))
print(len(a))
a.add(100)
print(a)
a.remove(10)
print(a)



