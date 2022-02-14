from typing import Dict
from urllib.parse import urljoin

from base.response import ScrapedResponse


class WatchAsianSearchResult(ScrapedResponse):
    def __init__(self, website: str, link: str, image: str, title: str) -> None:
        self.website = website
        self.uri = link
        self.link = urljoin(website, link)
        self.image = image
        self.title = title

    def json(self) -> Dict:
        """
        Return as JSON Dictionary Response.
        """

        return {
            "link": self.link,
            "image": self.image,
            "title": self.title,
            "uri": self.uri,
            "website": self.website,
        }
