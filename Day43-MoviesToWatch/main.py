from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
data = response.text

soup = BeautifulSoup(data, "html.parser")
movie_names = soup.find_all(name="h3", class_="title")
movie_title = [name.getText() for name in movie_names]
updated_list = movie_title[::-1]
with open("movies.txt","w",encoding="utf-8") as file:
    for name in updated_list:
        file.write(f"{name}\n")