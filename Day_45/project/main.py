
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h3", class_="title").get_text()

movie_list = [title.getText() for title in soup.find_all(name="h3",class_="title")]
movie_list.reverse()

with open("movies.txt",mode='w',encoding="utf-8") as file:
    
    for movie in movie_list:
        file.write(f"{movie}\n")