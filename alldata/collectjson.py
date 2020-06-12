import requests
import json

movie_info=[]
for i in range(10):
    pagenum = i+1
    url = f'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=a1e71f258fb351b1fa0a4af028ec8a17&language=ko&page={pagenum}'
    res = requests.get(url).json()
    
    movie_info.extend(
        res['results']
    )

with open('movies.json', "w", encoding="utf-8") as make:
    json.dump({'movie_info': movie_info}, make, indent='\t') 
