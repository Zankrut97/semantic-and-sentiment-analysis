import json
import pandas as pd

#List taken to store the data of tweets
glblist = {}
glbpol = {}
glbtwt = {}
word_dict = {}
twt_table_list=[]

#reading the tweets/Messages from tweets.json file 
with open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Sentiment Analysis\tweets.json') as f:
    data = json.load(f)

#Reading the words.csv which contains words and its polarity: https://sentic.net/downloads/
df = pd.read_csv(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Sentiment Analysis\words.csv')

#Storing words and it polarity into dictionary 
for ind in df.index:
     word_dict.update({df['CONCEPT'][ind]:df['POLARITY'][ind]})
     
#creating bag of words for each tweet/messages: https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php
for tweet in data:
    tweet_row=[]
    match_words=[]
    pos_freq=0
    neg_freq=0
    twt_polarity=""
    twt=tweet['tweet']
    frequency = dict()
    values = twt.split()
    for value in values:
        if value in frequency:
            frequency[value]+=1
        else:
            frequency[value]=1
    for words,freq in frequency.items():
            if words in word_dict:
                #matching bag of words with the dictionary containing the words and polarity and storing matched words in dictionary
                match_words.append(words) 
                if words not in glbpol.keys():
                    glbpol[words] = word_dict.get(words)
                if words not in glblist.keys():
                    glblist[words] = 1
                else:
                    glblist[words] = glblist[words] +1
                #calulating total postive frequency    
                if(word_dict.get(words)=='positive'):
                    pos_freq +=freq
                #calulating total postive frequency    
                elif(word_dict.get(words)=='negative'):
                    neg_freq +=freq         
    #calulating total polarity of the tweet
    if(pos_freq>neg_freq):
        twt_polarity = "POSITIVE"
    elif(pos_freq<neg_freq):
         twt_polarity = "NEGATIVE"
    elif(pos_freq==neg_freq):
         twt_polarity = "NEUTRAL"
    #appending data of one tweet into the list
    tweet_row.append(twt)
    tweet_row.append(match_words)
    tweet_row.append(pos_freq)
    tweet_row.append(neg_freq)
    tweet_row.append(twt_polarity)
    #appending that list into another list to create the csv table
    twt_table_list.append(tweet_row)   
#print(twt_table_list)
#print(len(twt_table_list))
df = pd.DataFrame(twt_table_list,columns=['Tweets/Message','Matched Words','Positive Word Frequency','Negative Word Frequency','Tweet Polarity'])
#creating tweet_polarity_table using df.to_csv() method
df.to_csv(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Sentiment Analysis\tweet_polarity_table.csv',index=False)

ll=[]
for x in glblist.keys():
    #print(x +" "+str(glblist[x])+" "+glbpol[x])
    ll.append([x ,glblist[x],glbpol[x]])
df = pd.DataFrame.from_records(ll, columns=["Word","Frequency","Polarity"])
#creating tweet_polarity_table using df.to_csv() method
df.to_csv(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Sentiment Analysis\word_cloud_output.csv',index=False)
    

