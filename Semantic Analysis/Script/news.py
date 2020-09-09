import requests
import json
import string
import re
import math
from prettytable import PrettyTable
from decimal import Decimal

API_KEY = '0f4a5d91c7684e90bbc9cc0ccd4acb90'
url = 'https://newsapi.org/v2/everything?'
Keywords = {'Canada','University','Dalhousie University','Halifax','Canada Education','Moncton','Toronto'}
news_articles=[]
cleaned_articles=[]

#Functions for cleaning the Data
def remove_punctuation(text):
    #reference for regex:https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    #print("removing punctuation")
    clean_text = text.translate(str.maketrans(dict.fromkeys(string.punctuation)))
    return clean_text

def remove_url(text):
    #reference for regex:https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
    #print("removing url")
    clean_text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text)
    return clean_text

for keyword in Keywords:
    parameters = {
        'q': keyword, 
        'pageSize': 20, 
        'apiKey': API_KEY 
    } 
    response = requests.get(url,params=parameters)
    response = json.dumps(response.json())
    response = json.loads(response)
    articles = response['articles']
    for article in articles:
        news_articles.append(article)
#print(news_articles)
        
j=1        
for news in news_articles:
        cleaned_articles=""
        #removing punctuation, url from title
        news['title'] = remove_punctuation(news['title'])
        news['title'] = remove_url(news['title'])
        news['title'] = news['title'].replace("\n","")
        news['title'] = news['title'].replace("\r","")
        news['title'] = "".join(i for i in news['title'] if ord(i)<128)
        news['title']=news['title'].lower()
        #removing punctuation, url from description
        news['description'] = remove_punctuation(news['description'])
        news['description'] = remove_url(news['description'])
        news['description'] = news['description'].replace("\n","")
        news['description'] = news['title'].replace("\r","")
        news['description'] = "".join(i for i in news['description'] if ord(i)<128)
        news['description']=news['description'].lower()
        #replacing None type with NO_VALUE
        if news['content'] is None:
            news['content'] = "NO_VALUE"
        #removing punctuation, url from content    
        news['content'] = remove_punctuation(news['content'])
        news['content'] = remove_url(news['content'])
        news['content'] = news['content'].replace("\n","")
        news['content'] = news['title'].replace("\r","")
        news['content'] = "".join(i for i in news['content'] if ord(i)<128)
        news['content']= news['content'].lower()
        cleaned_articles = news['title']+" "+news['description']+" "+news['content']
        #print(cleaned_articles)
        file = open(r'C:\Users\ZANKRUT THAKKAR\Desktop\MACS\Data Management Warehousing Analytics\Assignment - 4\Semantic Analysis\Articles\{0}.txt'.format(j), 'w')
        file.write(cleaned_articles)
        file.close
        j+=1

