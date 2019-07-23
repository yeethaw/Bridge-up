#libraries
import json

#opening file
file = open("survey_data.json","r")
data = json.load(file)
file.close()

countries =[]
for i in range(len(data)):
    user = data[i]
    user_country = user['country']
    countries.append(user_country)

#totalSum= sum(ages)
#average = totalSum/len(ages)
#print(average)

print(countries)
