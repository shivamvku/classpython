# # Files
# # ==========================

# # open()-> open('filename.extion','mode',encoding)
# # close()

# # fileobj = open('log.txt','w')
# # fileobj.write(''' Moody's Investors Service downgraded Tata Motors' corporate family rating (CFR) to Ba2 from Ba1

# # Vedanta: Company has been identified as the 'H1 qualified interested bidder' as per the bid process of the consortium of lenders of GMR Chhattisgarh Energy Limited (GCEL) for sale of controlling equity stake and restructuring of debt in GCEL.

# # City Union Bank allotted bonus shares in ratio 1:10''')
# # fileobj.close()






# fileobj = open('log.txt','r')
# # print(fileobj.read(134))
# print(fileobj.readline())
# print(fileobj.readline())
# print(fileobj.readline())
# print(fileobj.readline())
# print(fileobj.readline())
# fileobj.close()




# File I/O formating styles

# a = 'superam'
# b = 'Ironman'

# print('hello %s and %s'%(a,b))
# print('hello %d and %d'%(34453,321234))
# print('hello %f and %f'%(45645.5756,234234.23432))


# faincer formating styles
# new formating styles

# .format()

# a = 'superam'
# b = 'Ironman'
# # print('hello {1} and {0}'.format(a,b))
# # print('hello {1} and {3} have scored {0} and {2} respectivly'.format(a,b,45.234234,99.545))
# print('hello {:.2} and {:.3} preciois socres are {:.2f} and {:.2f}'.format(a,b,78.5675,55.783453))


