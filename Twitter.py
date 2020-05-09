from textblob import TextBlob
import sys
import tweepy
from tweepy import OAuthHandler
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100* float(part)/float(whole)

consumer="s1YqtJUWVmlE8t19oUqmW2b1I"
consumerSecrate="YooTuaeQWaJ2y6FeYqXZ7fhLOOoQQv8lNHbynR7Gup9y3OVmRd"    
accessToken="1171558387110121472-BxWl7CkzzVOlIxz94LzdCzDFV87b0g"
accessTokenSecrate="nhyHkybk4X19sC7MOF1eGdCUy6mspLdhcplOvLgrJUOiv"

auth=tweepy.OAuthHandler(consumer,consumerSecrate)
auth.set_access_token(accessToken,accessTokenSecrate)
api=tweepy.API(auth)

searchTerm = input("Enter a term\hastage for search:-")
noOfSearch = int(input("Enter the number of search:-"))

tweets=tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearch)

polarity=0
negetive=0
positive=0
neutral=0

for tweet in tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    polarity +=analysis.sentiment.polarity

    if(analysis.sentiment.polarity > 0.00):
        positive +=1
    
    elif(analysis.sentiment.polarity == 0.00 ):
        neutral +=1
    
    
    elif(analysis.sentiment.polarity < 0.00 ):
        negetive +=1
    

positive=percentage(positive, noOfSearch)
neutral=percentage(neutral, noOfSearch)
negetive=percentage(negetive, noOfSearch)
polarity=percentage(polarity, noOfSearch)
        

positive=format(positive,'.2f')
neutral=format(neutral,'.2f')
negetive=format(negetive,'.2f')



print("How people react on " +searchTerm+ " By analysing " +str(noOfSearch)+ ".Tweets")

if(polarity > 0.00):
    print("positive")
elif(polarity == 0):
    print("neutral")  
elif(polarity < 0.00 ):
    print("negetive")      


label=['positive ['+str(positive)+'%]', 'neutral['+str(neutral)+'%]' ,'negetive['+str(negetive)+'%]']
sizes=[positive,neutral,negetive]
colors=['yellowgreen','gold','blue']
print(sizes)
print(colors)
patches, texts=plt.pie(sizes,colors=colors, startangle=90)
plt.legend(patches, label, loc='best')
plt.title("How people react on " +searchTerm+ " By analysing " + str(noOfSearch)+ ".Tweets")
plt.axis('equal')
plt.tight_layout()
plt.show()
