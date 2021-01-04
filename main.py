from bs4 import BeautifulSoup
import requests
from pprint import pprint

top100_url = 'https://www.empireonline.com/movies/features/best-movies-2/'
top100_html = requests.get(top100_url).text

soup = BeautifulSoup(top100_html, 'html.parser')
movies_raw = soup.find_all(class_='title', name='h3')
movie_titles = []

for title in movies_raw:
    try:
        movie_title = title.text.split(') ')[1]
    except IndexError:
        movie_title = title.text
    movie_titles.append(str(movie_title.encode("ASCII", 'ignore'))[1:])
#pprint(movie_titles)

# for i in range(1, 101):
#     print("No: " + str(i) + " - " + str(101-i))

with open("movies.txt", "w") as file:
    for i in range(1, 101):
        #print(i)
        file.write(f"{i}) {movie_titles[100-i]} \n")

print(".")
