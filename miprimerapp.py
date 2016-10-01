array=[]

while 1:
	m=raw_input('poner nombre de un alumno o exit')
	if m == 'exit':
	  break 
	else:
	  array.append(m)
	


for i in range(len(array)):
	print 'tiene un alumno llamado ' +array[i]



print'usted tiene ' +str(len(array))+ ' alumnos'  




