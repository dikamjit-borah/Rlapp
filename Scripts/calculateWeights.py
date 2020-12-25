import pandas as pd
import numpy as np
import csv
import math
import csv

dataFile = pd.read_csv('coordinates.csv')

#x = (dataFile.loc[0,'x_Coordinate'])
#distance = []
#for i in range(0, len(dataFile)):
    #print(dataFile.loc[i,'x_Coordinate'])
    
#distance = math.sqrt( ((dataFile.loc[0,'x_Coordinate']-dataFile.loc[0,'y_Coordinate'])**2)+((dataFile.loc[1,'x_Coordinate']-dataFile.loc[1,'y_Coordinate'])**2) )
#print(x)
print(len(dataFile))

with open('Node_Distances_random.csv', 'w', newline = '') as distanceFileCSV:
	fileReader = csv.reader(distanceFileCSV)
	fileWriter = csv.writer(distanceFileCSV)
	fileWriter.writerow(['NODE A', 'NODE B', 'DISTANCE'])
	for i in range(len(dataFile)):
		for j in range(i, len(dataFile)):
			if(i!=j):
				fileWriter.writerow([i+1, j+1, 0])
	
distanceFile = pd.read_csv('Node_Distances_random.csv')

distance = []
for i in range(len(dataFile)):
    for j in range(i, len(dataFile)):
        if(i!=j):
            m_dist = abs(dataFile.loc[i, 'x_Coordinate'] - dataFile.loc[j, 'x_Coordinate']) + abs(dataFile.loc[i, 'y_Coordinate'] - dataFile.loc[j, 'y_Coordinate'])
			#print(m_dist + "\n")
            distance.append(int(m_dist))		
            #distanceFile['Distance'][i] = (math.sqrt(((dataFile.loc[i,'x_Coordinate']-dataFile.loc[i,'y_Coordinate'])**2)+((dataFile.loc[j,'x_Coordinate']-dataFile.loc[j,'y_Coordinate'])**2) ))

distanceFile['DISTANCE'] = distance

distanceFile.to_csv('Node_Distances_Random.csv')
