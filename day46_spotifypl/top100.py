import requests
from bs4 import BeautifulSoup


def top100(date):
    url = f"https://www.billboard.com/charts/hot-100/{date}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    return [song.find(name="h3") for song in soup.find_all(name="li", class_="o-chart-results-list__item") if
            song.find(name="h3")]
