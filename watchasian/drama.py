from typing import Dict, List

from base.response import ScrapedResponse


class WatchAsianDrama(ScrapedResponse):
    def __init__(self, url: str, title: str, image: str, episodes: List[Dict]) -> None:
        self.url = url
        self.title = title
        self.image = image
        self.episodes = episodes

    def json(self) -> Dict:
        """
        Return as JSON Dictionary Response.
        """
        return {"title": self.title, "image": self.image, "episodes": self.episodes}


class WatchAsianDramaEpisode(ScrapedResponse):
    def __init__(self, url: str, title: str, category: str, download: str) -> None:
        self.url = url
        self.title = title
        self.category = category
        self.download = download

    def json(self) -> Dict:
        """
        Return as JSON Dictionary Response.
        """
        return {
            "url": self.url,
            "title": self.title,
            "category": self.category,
            "download": self.download,
        }
