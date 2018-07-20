# a = ()
# a = (1,)
# a = 1,2,3,4,5,5
# print(type(a))

# varbale lenghr argumnnet or arbiatary argument
# --------------------------------------------------
# def greet(*names):
# 	# print(names)
# 	# print(type(names))
# 	for i in names:
# 		print('wwelcom {} to Digitalllync'.format(i))

# greet('batman','superman','Ironman','Wonderwomen')


# # op/
# wlecom batman to D
# wlecom batman to D
# wlecom batman to D
# wlecom batman to D


# Type-2 varbale lenghr argument

# def details(**info):
# 	# print(info)
# 	for i in info:
# 		print('wlecom %s from %s'%(i,info[i]))
# details(batman = 'Usa',Ironman = 'India',hulck= 'Pakistan')






# lambda expression or anonmys function

# syntaz

# var = lambda arg:expression-------- fun defination
# var(parmeters)------------> fun call

# squ = lambda num:num**2
# print(squ(3))


# map(fun,seq)-------------? 
# filter(fun,seq)
lst = [i for i in range(0,16)]
print(lst)

odd =  list(map(lambda i: i%2 != 0,lst))
print(odd) 


odd =  list(filter(lambda i: i%2 != 0,lst))
print(odd) 

