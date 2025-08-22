import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
web_html = response.text
print(web_html)

soup = BeautifulSoup(web_html,"html.parser")
#print(soup.prettify())
movies = soup.find_all(name="h3",class_="title")
print(movies)
movie_titles = [titles.getText() for titles in movies]
#print(movie_titles)
all_movies = movie_titles[::-1]
print(all_movies)

with open("movies.txt","w") as f:
    for movie in all_movies:
        f.write(f"{movie} \n")

