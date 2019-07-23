#libraries
import json

#list of dictionaries
users = []

#questions
questions = ["What is your name?",'What is your favorite food?','What city are you from?','How old are you?','Do you enjoy coding?','What country is your family from?',"What's your favorite movie?","What's your favorite meme?","What's your favorite candy?"]
#so we can identify which answers go to which question
keys = ['name','food','city','age','code','country','movie','meme','candy']


while True:
    #holds answers for user
    user = {}

    #goes through questions for user to answer
    for i in range(len(questions)):
        answer = input(questions[i])
        answer.lower()
        user[keys[i]] = answer

    #adds answers to list of dictionaries
    users.append(user)

    #asks if the user wants to continur
    end = input("Do you want to continue? yes / no :")
    end.lower()
    if end == 'no':
        file = open("survey_data.json" , "r")
        old_data = json.load(file)
        users.extend(old_data)
        file.close()
        file = open("survey_data.json" , 'w')
        json.dump(users , file)
        file.close()
        break
    else:
        continue
