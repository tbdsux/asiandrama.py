from typing import Dict, List


class WatchAsianDrama:
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

    def __repr__(self) -> str:
        return str(self.json())


class WatchAsianDramaEpisode:
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

    def __repr__(self) -> str:
        return str(self.json())
