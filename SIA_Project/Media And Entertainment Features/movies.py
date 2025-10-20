import requests

base_url = "http://www.omdbapi.com/?apikey=ac6ab35e&"

movie_title = "Game of Thrones"

def get_movie_data(title):
    response = requests.get(base_url + "t=" + title)
    if response.status_code == 200:
        return response.json()
    else:
        return None

movie_data = get_movie_data(movie_title)
if movie_data:
    print("Title:", movie_data.get("Title"))
    print("Year:", movie_data.get("Year"))
    print("Released:", movie_data.get("Released"))
    print("Genre:", movie_data.get("Genre"))
    print("Director:", movie_data.get("Director"))
    print("Plot:", movie_data.get("Plot"))
    #print("Poster URL:", movie_data.get("Poster"))
    print("IMDB Rating:", movie_data.get("imdbRating"))
else:
    print("Failed to retrieve movie data.")
