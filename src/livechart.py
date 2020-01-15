import requests
import os
from bs4 import BeautifulSoup

class LiveChart:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
        self.animes = []

    def result(self, url):
        page = requests.get(url, headers=self.headers)
        content = BeautifulSoup(page.content.decode(), "html.parser")
        articles = content.find_all("article", attrs={"class": "anime"})

        for article in articles:
            self.animes.append(self.get_anime(article))

        return self.animes

    def get_anime(self, content):
        return {
            "title": self.get_text_content(content.find("a", attrs={"data-target": "anime-card.mainTitle"})),
            "score": self.get_text_content(content.find("div", attrs={"class": "anime-avg-user-rating"})),
            "tags": self.get_tags(content.find("ol", attrs={"class": "anime-tags"}).find_all("li")),
            "premiere": self.get_text_content(content.find("div", attrs={"class": "anime-date"})),
            "countdown": self.get_episode_countdown(content.find("div", attrs={"class": "episode-countdown"})),
            "studio": self.get_text_content(content.find("a", attrs={"data-target": "anime-card.studioLink"})),
            "source": self.get_text_content(content.find("div", attrs={"class": "anime-source"})),
            "episodes": self.get_text_content(content.find("div", attrs={"class": "anime-episodes"})),
            "synopsis": self.get_text_content(content.find("div", attrs={"class": "anime-synopsis"})),
            "image_src": content.find("img").get("src")
        }

    def get_tags(self, content):
        tags = []
        for tag in content:
            tags.append(tag.find("a").text)
        
        return tags

    def get_episode_countdown(self, content):
        if content != None:
            episode_label = content.find("span", attrs={"class": "episode-label"}).text
            episode_timestamp = content.find("time").text

            return episode_label + ": " + episode_timestamp
        
        return None

    def get_text_content(self, content):
        if content == None:
            return None
    
        return content.text
