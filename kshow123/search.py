from typing import Dict

from base.response import ScrapedResponse


class KShowSearchResult(ScrapedResponse):
    def __init__(self, title: str, image: str, link: str) -> None:
        self.title = title
        self.image = image
        self.link = link

    def json(self) -> Dict:
        """
        Return as JSON Dictionary Response.
        """

        return {
            "link": self.link,
            "image": self.image,
            "title": self.title,
        }
