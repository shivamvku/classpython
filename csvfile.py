# a = open('sample.csv','w')
# a.close()


 # reader(...)
 #        csv_reader = reader(iterable [, dialect='excel']
 #                                [optional keyword args])
 #            for row in csv_reader:
 #                process(row)


 # writer(...)
 #        csv_writer = csv.writer(fileobj [, dialect='excel']
 #                                    [optional keyword args])
 #            for row in sequence:
 #                csv_writer.writerow(row)
        
 #            [or]
        
 #            csv_writer = csv.writer(fileobj [, dialect='excel']
 #                                    [optional keyword args])
 #            csv_writer.writerows(rows)


import csv

# def pen(fileobj,data):
# 	csv_writer = csv.writer(fileobj,delimiter = ',')
# 	for a in data:
# 		csv_writer.writerow(a)

def read(fileobj):
	csv_reader = csv.DictReader(fileobj,delimiter = ',')
	for row in csv_reader:
		print(row)
		# print

		(60*'-')

# DictReader()

if __name__ == '__main__':

	# fileobj = open('detais.csv','w')
	# data = ['Name,class,Phno,Adderss'.split(','),
	# 		'batman,python,4534654,usa'.split(','),
	# 		'superman,python,78978987,pakistan'.split(','),
	# 		'ironman,IoT,4544345643,bangladesh'.split(',')]
	# pen(fileobj,data)



"""paulsandeep.dl@gmail.com"""


	fileobj = open('detais.csv','r')
	read(fileobj)









