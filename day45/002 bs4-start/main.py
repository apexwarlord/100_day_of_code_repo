import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

story_spans = soup.find_all(name="span", class_="titleline")
scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
top_index = scores.index(max(scores))
top_story = story_spans[top_index].find("a")

print(top_story.getText() + ", " + top_story["href"])

# front_page = {score: story for score, story in zip(scores, story_spans)}
#
# for score, story in front_page.items():
#     print(story.find("a").getText() + "\nLink: " + story.find("a")["href"] + "\nScore: " + score)


# from bs4 import BeautifulSoup
#
# with open("website.html") as website:
#     contents = website.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# all_anchor_tags = soup.find_all(name="a")
# for anchor in all_anchor_tags:
#     print(anchor.get("href"))
#
# print(soup.find(name="h3", class_="heading"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
# name = soup.select_one(selector="#name")
# print(name.string + "\n\n\n")
#
# print(soup.select(".heading"))
#
