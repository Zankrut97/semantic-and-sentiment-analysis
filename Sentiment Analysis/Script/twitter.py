import tweepy as twp
import json
import string
import re
from datetime import datetime

API_KEY = 'cECrtDiWrYXGxNpMZ2DuWrLS5'
API_SECRET_KEY = 'pZKr5aayJz9bMjpAcdtyWY61gKDHkA0HbOFFa91ahs0ew6wh22'
ACCESS_TOKEN = '1232330596657049602-ByZPzLxGF5TviNMTNCDcDxBrdlOJaC'
ACCESS_TOKEN_SECRET = 'mg9ONnIcld7fwZE0YJ5LJQF56q0SWijXm6bhoIPaMfeio'

tweets = []
clean_tweets=[]

auth  = twp.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = twp.API(auth,wait_on_rate_limit=True)

twt=twp.Cursor(api.search,q='Canada OR University OR Dalhousie Univeristy OR Halifax OR Canada Education',lang='en',tweet_mode='extended',truncated=False).items(3500)


#Functions for cleaning the Data

def remove_punctuation(tweet_text):
    #reference for regex:https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    #print("removing punctuation")
    clean_tweet_text = tweet_text.translate(str.maketrans(dict.fromkeys(string.punctuation)))
    return clean_tweet_text

def remove_url(tweet_text):
    #reference for regex:https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
    #print("removing url")
    clean_tweet_text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', tweet_text)
    return clean_tweet_text

def remove_emoji(clean_tweet_text):
    #reference for unicodes: https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
    emoji_unicodes = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    #print("removing emoji")  
    clean_tweet_text = emoji_unicodes.sub(r'',clean_tweet_text)
    return clean_tweet_text

for keyword in twt:
    tweets.append(keyword)

for tweet in tweets:
    # to get the text of retweeted tweet    
    if "retweeted_status" in tweet._json:
        #collecting tweet text
         tweet_text = tweet.retweeted_status.full_text
        #removing urls from tweet text     
         clean_tweet_text = remove_url(tweet_text)
        #removing punctuation from tweet text
         clean_tweet_text = remove_punctuation(clean_tweet_text)
        #removing emoji from tweet text   
         clean_tweet_text = remove_emoji(clean_tweet_text)
         clean_tweet_text = clean_tweet_text.replace("\n","")
         clean_tweet_text = clean_tweet_text.replace("\r","")
         clean_tweet_text = "".join(i for i in clean_tweet_text if ord(i)<128)
         clean_tweets.append({"tweet":clean_tweet_text.lower()})
    else:
        tweet_text = tweet.full_text
        clean_tweet_text = remove_url(tweet_text)
        clean_tweet_text = remove_punctuation(tweet_text)
        clean_tweet_text = remove_emoji(clean_tweet_text)
        clean_tweet_text = clean_tweet_text.replace("\n","")
        clean_tweet_text = clean_tweet_text.replace("\r","")
        clean_tweet_text = "".join(i for i in clean_tweet_text if ord(i)<128)
        clean_tweets.append({"tweet":clean_tweet_text.lower()})

with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\tweets.json', 'w') as f:
    json.dump(clean_tweets, f)

print("Json file generated")
