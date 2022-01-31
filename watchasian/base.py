from typing import List
from smaxpy import Smax
from urllib.parse import urljoin
from watchasian.drama import WatchAsianDrama

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

    def fetch_uri(self, uri: str) -> WatchAsianDrama:
        url = urljoin(self.__website, uri)

        client = self._get_client(url)
        query = client.find("div", class_="content").find("div", class_="content-left")

        _info = query.find("div", class_="info")
        _episodes = query.find("ul", class_="all-episode")
        _img = query.find("div", class_="img")

        # get data
        _title = _info.find("h1").text.strip()
        _image = _img.find("img")["src"]

        # TODO: this will be implemented soon
        # get info

        # get episodes
        eps = []
        for i in _episodes.find_all("li"):
            _ep = {}

            _ep["title"] = i.find("h3").text.strip()
            _ep["timestamp"] = i.find("span", class_="time").text.strip()
            _ep["sub_type"] = i.find("span", class_="type").text.strip()
            _ep["link"] = urljoin(self.__website, i.find("a")["href"])

            eps.append(_ep)

        return WatchAsianDrama(url, _title, _image, eps)
