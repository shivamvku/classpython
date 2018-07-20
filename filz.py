# # cursor opertion
# # seek(post,offset)---------> 
# # tell(post,offset)
# fileobj = open('today.txt','r')
# # fileobj.write(''' Moody's Investors Service downgraded Tata Motors' corporate fa
# # from Ba1Vedanta: Company has been identified as the 'H1 qualified interested bidder'
# # as per the bid process of the consortium of lenders of GMR Chhattisgarh Energy Limited  
# # sale of controlling equity stake and restructuring of debt in GCEL.
# # City Union Bank allotted bonus shares in ratio 1:10''')
# # po1 = fileobj.tell()
# # print(po1)
# # # fileobj.write('somting')
# po2 = fileobj.tell()
# print(po2)

# pos3 = fileobj.seek(0,0)
# print(pos3)

# # print(fileobj.read())

# pos4 = fileobj.seek(200)
# print(pos4)

# # fileobj.write('i am in middle')
# print(fileobj.read())
# fileobj.close()





# python dictorys


import os
from os import *

# os.mkdir('/home/vineet/Documents/i_am_too_dum')

# print(os.getcwd())

# os.chdir('/home/vineet/Documents/vineet/python/class_1200/i_am_too_dum')

# print(os.getcwd())



# rename('i_am_too_dum','reanmed')
rmdir('reanmed')

