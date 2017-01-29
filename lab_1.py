import csv
import plotly

#Abrimos la hoja de calculo con la trabajaremos
with open('student-mat.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=';')
	
	ages	= [] 
	g1		= [] 
 	g2		= []  
	
	for row in readCSV:
		age = row[2] 
		g1_data = row[30] 
		g2_data = [31]
		
		ages.append(age)
		g1.append(g1_data)
		g2.append(g1_data)
	
	print (ages)
	print ("\n\n")
	print (g1)
	print ("\n\n")
	print (g2) 

print "hola"
