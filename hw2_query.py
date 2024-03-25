from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import sys
from datetime import datetime
"""
Returns the movie listing corresponding to a given name
"""
def find_by_name(name : str, collection: MongoClient):
    movie_query = {"movie_name" : name}
    movie_docs = collection.find(movie_query)
    for doc in movie_docs:
        print(doc)


"""
Returns all movies with either positive or negative sentiment
"""
def find_by_sentiment( collection: MongoClient,audience : bool, positive: bool=True):
    if positive:
        sentiment = "positive"
    else:
        sentiment = "negative"
    if audience:
        who = "audience"
    else:
        who = "critic"
    movie_query = {(who+"_sentiment"): sentiment}
    movie_docs = collection.find(movie_query)
    for doc in movie_docs:
        print(doc)

"""
Returns all movies that opened either before or after a date 
"""    
def find_by_open_date(collection: MongoClient,date:datetime, before: bool=True):
    if before:
        operator = "lte"
    else:
        operator = "gte"
    movie_query = {"opening_date" : {operator: date}}
    movie_docs = collection.find(movie_query)
    for doc in movie_docs:
        print(doc)

def find_by_score(collection: MongoClient, audience : bool, score : int, greater: bool):
    if greater:
        operator = "gte"
    else:
        operator = "lte"
    if audience:
        who = "audience"
    else:
        who = "critic"
    movie_query = {(who+"_score"): {operator:score}}
    movie_docs = collection.find(movie_query)
    for doc in movie_docs:
        print(doc)

if __name__ == "__main__":
    client = MongoClient()
    db = client['rotten_tomatoes']
    first_object = {
        "Name": "David"
    }
    collection = db['scraped']
    count = 0
    for doc in collection.find():
        count = count+1
       # print(doc)
   #print(count)
    find_by_name("Madgaon Express", collection)
    find_by_sentiment(collection=collection, audience=True, positive=True)
    find_by_open_date(collection,datetime.today(),before=True)