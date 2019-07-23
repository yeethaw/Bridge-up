#libraries
import json
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud

#loading tweet file
tweet_file = open('twitter_data.json' , 'r')
tweet_data = json.load(tweet_file)
tweet_file.close()

#lists needed
pol = []
sub =[]
tweets_string = ""

#goes through tweet data and adds polartity and subjectivity to lists
for tweet in tweet_data:
    text = TextBlob(tweet['text'])
    polarity = text.polarity
    subjectivity = text.subjectivity
    pol.append(polarity)
    sub.append(subjectivity)
    tweets_string = tweets_string + tweet['text']


#finds avg of polarity and subjectivity
sumpol = sum(pol)
sumsub = sum(sub)
avgpol = sumpol / len(pol)
avgsub = sumsub / len(sub)
print(avgpol , avgsub)


tweets = TextBlob(tweets_string)
tweets_words = tweets.words

filtered_tweets = {}
bad_words = []

for word in tweets_words:
    if len(word) <= 3:
        bad_words.append(word)
    elif word.isalpha() == False:
        bad_words.append(word)
    elif word == "https" or word == "http":
        bad_words.append(word)
    elif '.' in word:
        bad_words.append(word)
    else:
        word = word.lower()
        filtered_tweets[word] = tweets.word_counts[word]


cloudword = WordCloud().generate_from_frequencies(filtered_tweets)
plt.figure()
plt.imshow(cloudword, interpolation="bilinear")
plt.axis("off")
plt.show()



#POLARITY GRAPHS ---------------------------------------------------------------------------------

#creates graph
plt.hist (pol , 30 , color = 'hotpink')
plt.suptitle("Polarity of Tweets")
plt.xlabel(" polarity ")
plt.ylabel("frequency ")

#saves and shows graph
plt.savefig('tweets_polarity.png')
#plt.show()

#SUBJECTIVITY GRAPHS -------------------------------------------------------------------------------

#creates graph
plt.hist (sub , 30 , color = 'aquamarine')
plt.suptitle("Subjectivity of Tweets")
plt.xlabel("subjectivity")
plt.ylabel("frequency")

#saves and shows graph
plt.savefig('tweets_subjectivity.png')
#plt.show()
