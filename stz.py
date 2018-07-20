# Sets

# set is a cooletion of int , float, str complex nad tuple

# a = {key:value}
# {}
# a = {1,24,4,5,1,6}
# # set()
# print(type(a))
# print(a)
# Adding elemts in set
# ------------------------------
# b s= {1,24,4,5,1,6}

# b.pop()
# print(b)
# b.pop()
# # del b[]
# print(b)
# b.remove('superman')
# print(b)

# # a+b
# # 2*a
# st=  'DigitalLync'
# b = set(st)
# c = list(st)
# d = tuple(st)
# print(b)
# print(c)
# print(d)

# a = {i for i in range(0,11)}
# print('this is a=',a)
# b = {2,4,7,33,23,56}
# print('this is b=',b)

# print(a.union(b))
# print(a | b)

# print(a.intersection(b))
# print('this is interstion= ',a&b)

# print(a-b)
# print(b-a)

# print(a.difference(b))

# print(b.difference(a))





a = {i for i in range(0,11)}
print(type(a))
print(a)

frset = frozenset(a)
# print(type(frset))
# print(frset)
# b = tuple(frset)
# print(b)

print(min(frset))
print(max(frset))
print(sum(frset))