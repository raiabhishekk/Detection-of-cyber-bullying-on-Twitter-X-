import snscrape.modules.twitter as sntwitter
import pandas as pd

query="Nupur sharma"
tweets=[]
limit=100
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break

    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df= pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)
df.to_csv('tweets.csv')