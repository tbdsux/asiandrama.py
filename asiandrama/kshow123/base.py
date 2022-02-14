import json
import re
from urllib.parse import urljoin

from base.scraper import BaseAsianDramaScraper
from kshow123.search import KShowSearchResult
from kshow123.show import KShowShow, KShowShowEpisode


class KShow123(BaseAsianDramaScraper):
    def __init__(self) -> None:
        super().__init__("http://kshow123.net/")

    def search(self, query: str):
        """Search shows on KShow123

        Args:
            query (str): search query, show name

        Returns:
            [type]: [description]
        """
        query = query.replace(" ", "-")

        client = self._get_client(
            f"/search/{query}/"
        )  # NOTE: you need to add the trailing slash in here
        query = client.find("div", id="featured")

        # parse search results in here
        data = []
        for i in query.find_all("div", class_="col-md-3 col-xs-6 col-sm-3"):
            title = i.find("h2").text.strip()
            link = i.find("a")["href"]
            image = i.find("img")["src"]

            data.append(KShowSearchResult(title, image, link))

        return data

    def fetch_uri(self, url: str) -> KShowShow:
        """Fetch show on KShow123

        Do not include the base watchasian url. For example, only set
        `/drama-url-in-here` like so.

        Args:
            url (str): url of show

        Returns:
            KshowDrama
        """

        final_url = urljoin(self.website, url)

        client = self._get_client(url)
        query = client.find("div", id="content")

        _info = query.find("div", id="info")
        _episodes = query.find("div", id="list-episodes")

        # get data
        _title = _info.find("h1").text.strip()
        _img = _info.find("img")["src"]
        _desc = _info.find("div", class_="desc").text.strip()

        # get episodes
        eps = []
        for i in _episodes.find_all("tr"):
            _ep = {}

            _ep["title"] = i.find("h2").text.strip()
            _ep["timestamp"] = i.find(
                "td", class_="text-right text-muted hidden-xs"
            ).text.strip()
            _ep["sub_type"] = i.find("span", class_="label label-sub").text.strip()
            _ep["link"] = i.find("a")["href"]

            eps.append(_ep)

        return KShowShow(final_url, _title, _desc, _img, eps)

    def get_episode(self, url: str) -> KShowShowEpisode:
        """Fetch a show episode by its url.

        Do not include the base watchasian url. For example, only set
        `/drama-url-in-here/episode-1.html` like so.

        Args:
            url (str): show episode url

        Returns:
            KShowShowEpisode
        """

        final_url = urljoin(self.website, url)

        client = self._get_client(url)
        query = client.find("div", id="player")

        title = query.find("h1").text.strip()
        downloads = []

        script = None
        for i in client.find_all("script"):
            if "videoJson" in i.text:
                script = i

        rem = re.search("videoJson = (.*?);", script.string)
        if rem:
            t = rem.group(1)
            t = t.replace("\\", "").replace("'", "")

            downloads = json.loads(t)

        return KShowShowEpisode(final_url, title, downloads)
