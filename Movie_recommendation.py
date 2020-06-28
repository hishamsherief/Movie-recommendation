import requests
import json

def get_movies_from_tastedive(movie):
    #give your Access_key to testdrive as Access key1
    params = {'q':movie, 'type':'movies', 'limit':5, 'k':Access_key1} 
    result = requests.get("https://tastedive.com/api/similar", params = params)
    return result.json()

def extract_movie_titles(dic):
    result = []
    for i in dic['Similar']['Results']:
        result.append(i['Name'])
    return result

def get_related_titles(lst):
    #to get related movies
    result = []
    for i in lst:
        temp = extract_movie_titles(get_movies_from_tastedive(i))
        for n in temp:
            if n not in result:
                result.append(n)
    return result

def get_movie_data(movie):
    #give your access key to omdbapi as Access_key2
    result = requests.get("http://www.omdbapi.com/", params = {'t':movie, 'r':'json', apikey:access_key2})
    result = result.text
    return json.loads(result)

def get_movie_rating(dic):
    #to get movie rating from Rotten Tomatoes
    for r in dic['Ratings']:
        result = 0
        if r['Source'] == 'Rotten Tomatoes':
            result = int(r['Value'].replace('%',''))
            return result
    return result

def get_sorted_recommendations(lst):
    result = get_related_titles(lst)
    return sorted(result, key = lambda name:(get_movie_rating(get_movie_data(name)), name), reverse = True)
