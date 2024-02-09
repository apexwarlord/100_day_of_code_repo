import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20190701161408/https://www.empireonline.com/movies/features/best-movies-2/")

top_100 = response.text

soup = BeautifulSoup(top_100, "html.parser")

movies = soup.find_all(name="h2")

movie_list = [movie.getText() for movie in movies][::-1]

with open("move_list.txt", "w") as f:
    for movie in movie_list:
        f.write(movie + "\n")

# comp2019 = []
# for movie in movie_list:
#     edit = movie.split()
#     comp2019.append(" ".join(edit[1:-1]))
#
# print(comp2019)
#
# response2024 = requests.get(
#     "https://www.empireonline.com/movies/features/best-movies-2/")
#
# top_100_2024 = response2024.text
#
# soup = BeautifulSoup(top_100_2024, "html.parser")
#
# movies2024 = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
#
# movie_list2024 = [movie.getText() for movie in movies2024][::-1]
#
# comp2024 = []
# for movie in movie_list2024:
#     edit = movie.split()
#     comp2024.append(" ".join(edit[1:]))
#
# for movie in comp2024:
#     if movie not in comp2019:
#         print(movie)

# story_spans = soup.find_all(name="span", class_="titleline")
# scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# top_index = scores.index(max(scores))
# top_story = story_spans[top_index].find("a")
#
# print(top_story.getText() + ", " + top_story["href"])
