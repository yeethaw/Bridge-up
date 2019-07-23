import json

tweet_file = open('twitter_data.json' , 'r')
tweet_data = json.load(tweet_file)
tweet_file.close()

#print('Tweet id:' , tweet_data[0]['id'])

#print('Tweet text:', tweet_data[0]['text'])

#for i in range(len(tweet_data)):
#    print("Tweet text:" , tweet_data[i]['text'])

#for tweet in tweet_data:
#    print("Tweet text:" , tweet['text'])


for tweet in tweet_data:
    print("Tweet location:" ,tweet['location'])
