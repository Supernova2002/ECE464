from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import sys


if __name__ == "__main__":



    client = MongoClient()
    #print(client.list_database_names())
    db = client['test']
    first_object = {
        "Name": "David"
    }
    #first = db['first']
    #result = first.insert_one(first_object)
    #print(f"One insert: {result.inserted_id}")

    # for rotten tomatoes, look for tile-dynamic skeleton="panel"

    
    r = requests.get("https://www.rottentomatoes.com/browse/movies_in_theaters/?page=5")
    soup = BeautifulSoup(r.text, 'html.parser')
    movies = soup.findAll("tile-dynamic", skeleton="panel")
    count = 0
    for movie in movies:
        #audience_score = movie.find("score-pairs-deprecated").contents
        movie_name = str.strip(movie.find_all("span")[0].contents[0])
        opening_date = str.strip(movie.find_all("span")[1].contents[0])
        audience_score = [item['audiencescore'] for item in movie.find_all('score-pairs-deprecated', attrs={'audiencescore' : True})][0]
        audience_sentiment = [item['audiencesentiment'] for item in movie.find_all('score-pairs-deprecated', attrs={'audiencesentiment' : True})][0]
        critic_score = [item['criticsscore'] for item in movie.find_all('score-pairs-deprecated', attrs={'criticsscore' : True})][0]
        critic_sentiment = [item['criticssentiment'] for item in movie.find_all('score-pairs-deprecated', attrs={'criticssentiment' : True})][0]
      
        movie_object = {
            "movie_name" : movie_name,
            "opening_date" : opening_date,
            "audience_score": audience_score,
            "audience_sentiment": audience_sentiment,
            "critic_score": critic_score,
            "critic_sentiment": critic_sentiment
        }
        print(movie_object)
        count = count + 1

    print(count)