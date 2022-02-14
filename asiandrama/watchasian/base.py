from typing import List
from urllib.parse import urljoin

from base.scraper import BaseAsianDramaScraper

from .drama import WatchAsianDrama, WatchAsianDramaEpisode
from .search import WatchAsianSearchResult


class WatchAsian(BaseAsianDramaScraper):
    def __init__(self, website: str):
        super().__init__(website)

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

            data.append(WatchAsianSearchResult(self.website, link, image, title))

        return data

    def fetch_uri(self, url: str) -> WatchAsianDrama:
        """Fetch dramas, shows or movies with their url.

        Do not include the base watchasian url. For example, only set
        `/drama-url-in-here` like so.

        Args:
            url (str): url of drama / show / movie

        Returns:
            WatchAsianDrama
        """

        final_url = urljoin(self.website, url)

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
            _ep["link"] = urljoin(self.website, i.find("a")["href"])

            eps.append(_ep)

        return WatchAsianDrama(final_url, _title, _image, eps)

    def get_episode(self, url: str) -> WatchAsianDramaEpisode:
        """Fetch a drama, show or movie episode with its url.

        Do not include the base watchasian url. For example, only set
        `/drama-url-in-here/episode-1.html` like so.

        Args:
            url (str): drama / show / movie episode url

        Returns:
            WatchAsianDramaEpisode
        """

        final_url = urljoin(self.website, url)

        client = self._get_client(url)
        query = client.find("div", class_="block watch-drama")

        _title = query.find("h1").text.strip()
        _category = query.find("div", class_="category").find("a").text.strip()
        _download = query.find("li", class_="download").find("a")["href"]

        if not _download.startswith("https://"):
            _download = "https:" + _download

        return WatchAsianDramaEpisode(final_url, _title, _category, _download)
