import pandas as pd
from requests import get
from bs4 import BeautifulSoup
import numpy as np
import requests
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px

headers = {"Accept-Language": "en-US, en;q=0.5"}

url = "https://www.imdb.com/search/title/?release_date=2021-01-01,&count=1000"

results = requests.get(url, headers = headers)

bsoup = BeautifulSoup(results.text , "html.parser")

titles = []

IMDB_ratings = []

ratings = []

genres = []

runtimes = []

notable_figs = []

descriptions = []

movies_divs = bsoup.find_all('div', class_= 'lister-item mode-advanced')

for container in movies_divs:

    title = container.h3.a.text
    titles.append(title)

    rating = container.find('span', class_= 'certificate').text if container.p.find('span', class_='certificate') else 'Not Rated'
    ratings.append(rating)

    runtime = int(container.find('span', class_= 'runtime').text.strip().replace(" min","")) if container.p.find('span', class_='runtime') else None
    runtimes.append(runtime)

    genre = container.find('span', class_= 'genre').text.strip().replace('\n','') if container.p.find('span', class_='genre') else ''
    genres.append(genre)

    imdb_rat = float(container.strong.text) if container.find('strong') else 'N/A'
    IMDB_ratings.append(imdb_rat)

    stars = container.find('p', class_="").text.strip().replace("\n",'').replace("Director:","").replace("Stars:","").split("|", 1)
    notable_figs.append(stars)

    description = container.find_all('p', class_= "text-muted")[1].text.replace("\n",'').strip()
    descriptions.append(description)




df = pd.DataFrame({
    'movie': titles,
    'rating': ratings,
    'runtime(min)': runtimes,
    'genres': genres,
    'IMDB_rating':IMDB_ratings,
    'actors': notable_figs,
    'description': descriptions})


