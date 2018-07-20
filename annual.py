# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Annual_NY_CloudCover_csv.csv')

#print(df.head(6))

year = df['Year']
total = df['Total Cloud Cover']
temp = df['Temperature �']
rad = df['Daily Shortwave Radiation']

plt.plot (year , total, color = 'red')
plt.legend (loc = 'bottom left')
plt.twinx()
plt.plot (year, temp , color = 'blue' )

plt.title ('Total Cloud Cover and Temperature')
plt.xlabel('years')
plt.xticks(range(1985 , 2018 , 10))
plt.xlim (1985, 2018)

plt.legend(loc = 'best')

plt.savefig(' Cloud cover and temp.png')
plt.show()

plt.plot (year, rad , color = 'pink')

plt.title('Daily Radiation')
plt.xlabel ('Years')
plt.xticks(range(1985 , 2018 ,10))
plt.xlim (1985, 2018)

plt.legend(loc = "best")

plt.savefig('Daily radssss.png')
plt.show()