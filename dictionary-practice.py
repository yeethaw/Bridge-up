users = {
    'veronika':17,
    'alex':17,
    'danie':15,
    'julia':15,
    'mom':37,
    'vlad':16,
    'emma':16,
    'grant':16,
    'oniva':17,
    'the doctor':-3
}

users['carrie'] = 20

users['harika'] = 21

for user in users:
    if users[user] > 15 and users[user] < 20:
        print(user + ' is a teenager')
    elif users[user] <= 15 and users[user] >= 0:
        print(user +' is a youngster')
    elif users[user] >= 20:
        print(user + ' is an adult')
    elif users[user] >= 50:
        print(user + ' is a goldie oldie')
    else:
        print(user + ' is void of the constructs of age')

print(users)

firstlast = {
    "Jason":"Todd",
    "Tim":"Drake",
    "Bruce":"Wayne",
    "Clark":"Kent",
    "Emma":"Brown"
}

print(firstlast)
