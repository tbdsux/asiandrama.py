from typing import List
from smaxpy import Smax
from urllib.parse import urljoin

from watchasian.search import WatchAsianSearchResult


class WatchAsian:
    def __init__(self, website: str):
        self.__website = website

    def _get_client(self, uri: str) -> Smax:
        return Smax(urljoin(self.__website, uri))

    def search(self, query: str) -> List[WatchAsianSearchResult]:
        """Search for dramas, shows or movies.

        Args:
            query (str): title of drama / show / movie

        Returns:
            List[WatchAsianSearchResult]
        """

        client = self._get_client(f"search?type=movies&keyword={query}")
        query = client.find("div", class_="block tab-container")

        data: List[WatchAsianSearchResult] = []

        for i in query.find_all("li"):
            link = i.find("a")["href"]
            image = i.find("img")["data-original"]
            title = i.find("h3").text.strip()

            data.append(WatchAsianSearchResult(self.__website, link, image, title))

        return data
