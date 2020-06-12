import requests
import json

with open('movies.json', 'r', encoding='utf-8') as m:
    mdata = json.load(m)

with open('genre.json', 'r', encoding='utf-8') as g:
    gdata = json.load(g)

movies = []
for i, data in enumerate(mdata.get("movie_info")):
    movie = dict()
    fields = dict()

    movie["pk"] = i + 1
    movie["model"] = "movies.movie"
    
    fields["title"] = data.get("title")
    fields["original_title"] = data.get("original_title")
    fields["overview"] = data.get("overview")
    fields["poster_path"] = data.get("poster_path")
    fields["backdrop_path"] = data.get("backdrop_path")
    fields["release_date"] = data.get("release_date")
    fields["popularity"] = data.get("popularity")
    fields["vote_count"] = data.get("vote_count")      
    fields["vote_average"] = data.get("vote_average")
    fields["adult"] = data.get("adult")
    fields["users_like"] = []

    genres = []
    for j in range(len(data.get("genre_ids"))):
        genres.append(data["genre_ids"][j])
    
    fields["genres"] = genres
    movie["fields"] = fields
    movies.append(movie)


genres = []
for i, data in enumerate(gdata.get('genres')):
    genre = dict()
    fields = dict()
    genre["pk"] = data.get("id")
    genre["model"] = "movies.genre"
    fields["name"] = data.get("name")
    genre["fields"] = fields
    genres.append(genre)


with open('final_movies.json', 'w', encoding='utf-8') as make_m:
    json.dump(movies, make_m, indent='\t')

with open('final_genres.json', 'w', encoding='utf-8') as make_g:
    json.dump(genres, make_g, indent='\t')


