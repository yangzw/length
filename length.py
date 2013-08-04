'''
length for Code Marathon
python
ubuntu  12.04
by yangzw
2013.8.4
'''
import string
import re

#the dict to record the trans of diff unit
record = {'m':1}

#get the trans
def get_tran(line):
	# asume the format must be "1 ** = ** m" as your input.txt shows
	tmp = line.split(' ')[1:5:2]
	f_value = string.atof(tmp[1])
	record[tmp[0]] = f_value 
	#use more space to save time
	record[tmp[0] + 's'] = f_value 
	record[tmp[0] + 'es'] = f_value 
	record[tmp[0].replace("oo","ee")] = f_value 
	record[re.sub(r'f[e]?$','ves',tmp[0])] = f_value
	record[re.sub(r'y$','ies',tmp[0])] = f_value

#calculate
def calculate(line):
	sun = 0.0;
	array = line.split(' ')
	length = len(array)
	i = 0
	while i < length:
		if array[i] == '+':
		        i += 1
			sun += string.atof(array[i])*record[array[i+1]]
		elif array[i] == '-':
			i += 1
			sun -= string.atof(array[i])*record[array[i+1]]
		else:
			sun = string.atof(array[i])*record[array[i+1]]
		i += 2
	outfile.write("%.2f m\n" % sun)

myfile = open("input.txt","r")
outfile = open("output.txt","w")
outfile.write("yangz_w@outlook.com\n\n")
flag = 0;
for line in myfile:
	line = line.strip('\n')
	if(flag == 0):
		if(line == ''):
			flag = 1;
		else:
			get_tran(line)
	elif(line != ''):
			calculate(line)
myfile.close()
outfile.close()
