from typing import Dict, List

from base.response import ScrapedResponse


class KShowShow(ScrapedResponse):
    def __init__(
        self, url: str, title: str, description: str, image: str, episodes: List[Dict]
    ) -> None:
        self.url = url
        self.title = title
        self.image = image
        self.episodes = episodes
        self.description = description

    def json(self) -> Dict:
        """
        Return as JSON Dictionary Response.
        """
        return {
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "episodes": self.episodes,
        }


class KShowShowEpisode(ScrapedResponse):
    def __init__(self, url: str, title: str, downloads: List[Dict]) -> None:
        self.url = url
        self.title = title
        self.downloads = downloads

    def json(self) -> Dict:
        """
        Return as JSON Dictionary Response.
        """
        return {"title": self.title, "url": self.url, "downloads": self.downloads}
