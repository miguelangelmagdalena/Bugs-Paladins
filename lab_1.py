import csv
import plotly
plotly.tools.set_credentials_file(username='miguelmagdalena', api_key='R5lLl86vAwfjjNDaVFlO')
import plotly.graph_objs as go

#Abrimos la hoja de calculo con la trabajaremos
with open('student-mat.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=';')
	
	ages	= [] 
	g1		= [] 
	g2		= []  
	
	#Guardamos las edades y resultados de primer periodo g1 y segundo g2 
	for row in readCSV:
		age = row[2] 
		g1_data = row[30] 
		g2_data = row[31]
		
		ages.append(age)
		g1.append(g1_data)
		g2.append(g2_data)

#mostramos datos del csv
'''
print ("Edades de alumnos y resultados de examenes g1 y g2")
print (ages)
print ("\n\n")
print (g1)
print ("\n\n")
print (g2) 
'''

#Hacemos un diagrama de dispersion
trace = go.Scatter(
	x = g1,
	y = g2,
	mode = 'markers',
	name = 'Relacion entre G1 y G2',
	marker = dict(
		size 	= 10,
		color 	= 'rgba(152, 0, 0, .8)',
		line 	= dict(
			width = 2,
			color = 'rgba(0,0,0)'
		)
	)
)

data = [trace]

#plotly.plotly.iplot(data, filename = 'Diagrama de dispersion de resultados de examenes G1 y G2')

#Hacemos un histograma
ages2 = ages
unique_ages = []
total = []
tam1 = len(ages2)

#Buscamos las edades sin repetirse
unique_ages = list(set(ages))
i=0
#Contamos el total de cada edad
while(i< len(unique_ages)):
	cantidad = str(ages.count(unique_ages[i]))
	total.append(cantidad)
	i=i+1

#print(unique_ages)
#print("\n\n")
#print(total)

data2 = [go.Bar(
			x = unique_ages,
			y = total
		)]

plotly.plotly.iplot(data2,filename='Diagrama de barras de la edad')
