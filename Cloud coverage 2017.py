import numpy as np
import csv
import matplotlib.pyplot as plt


#2002 map
csvFile = open("CloudFraction1_2017.csv", 'r') 
csvReader = csv.reader(csvFile, delimiter=',')
data_lists_2002 = list(csvReader)

width_2002 = len(data_lists_2002[0])
height_2002 = len(data_lists_2002)

grid2002 = np.empty([height_2002, width_2002, 3], dtype=np.uint8)

all_values = [] # We will fill in this empty list with all the data values as we go

for r, row in enumerate(data_lists_2002):
   for c, value in enumerate(row):
       if float(value) < 99999:
           all_values.append(float(value)) # This is where we fill in the list with all data values
       if float(value) <= 0:
           grid2002[r, c] = [0, 97, 255] #Change [R,G,B]
       elif float(value) <= .1:
           grid2002[r, c] = [27, 113, 252]
       elif float(value) <= .2:
           grid2002[r, c] = [66, 138, 255]
       elif float(value) <= .3:
           grid2002[r, c] = [100, 158, 252]
       elif float(value) <= .4:
           grid2002[r, c] = [119, 171, 255]
       elif float(value) <= .5:
           grid2002[r, c] = [140, 184, 255]
       elif float(value) <= .6:
           grid2002[r, c] = [163, 198, 255]
       elif float(value) <= .7:
           grid2002[r, c] = [183, 210, 255]
       elif float(value) <= .8:
           grid2002[r, c] = [206, 224, 255]
       elif float(value) <= .9:
           grid2002[r, c] = [219, 232, 255]
       elif float(value) <= 1:
           grid2002[r, c] = [255, 255, 255]
       else:
           grid2002[r, c] = [109, 109, 109]
        
    

plt.title("Cloud Fraction in 2017")
plt.imshow(grid2002)
plt.axis('off')
plt.savefig("Cloud_Fraction_in_2017.png", dpi = 1000)
plt.show()