import csv
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *
#init_notebook_mode()
import numpy as np

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

#mostramos datos del csv
print ("Edades de alumnos y resultados de examenes g1 y g2")
print (ages)
print ("\n\n")
print (g1)
print ("\n\n")
print (g2) 


#hacemos algunos calculos con la data
'''
n= 1000
random_x = np.random.randn(n)
random_y = np.random.randn(n)

trace = Scatter(
	x = random_x,
	y = random_y,
	mode = 'markers'
)
data = [trace]
iplot(data)
'''
