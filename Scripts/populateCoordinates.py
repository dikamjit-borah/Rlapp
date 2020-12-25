import csv

filetC = open("topologyCoordinates.txt", "r")
for line in filetC:
	xy_both = line.split(";")

coor = []
coorArray = []
x_coor = []
y_coor = []

for i in range(0,len(xy_both)):
        coor.append(xy_both[i].split(" "))
        
for i in range(len(coor)):
        for j in coor[i]:
                coorArray.append(j)
for i in range(0, len(coorArray)):
        if(i%2 == 0):
                x_coor.append(coorArray[i])
        else:
                y_coor.append(coorArray[i])

with open('Node_Coordinates.csv', 'w', newline='') as coor_Csv:
        coor_CsvRead = csv.reader(coor_Csv)
        coor_CsvWrite = csv.writer(coor_Csv)
        coor_CsvWrite.writerow(['Node_Sl_No.', 'x_Coordinate', 'y_Coordinate'])

        for i in range(len(x_coor)-1):
                coor_CsvWrite.writerow([i, x_coor[i], y_coor[i]])
        
