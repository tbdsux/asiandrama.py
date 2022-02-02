from smaxpy import Smax
from urllib.parse import urljoin


class KShow123:
    def __init__(self) -> None:
        self.__website = "http://kshow123.net/"

    def _get_client(self, url: str) -> Smax:
        return Smax(urljoin(self.__website, url))

    def search(self, query: str):
        query = query.replace(" ", "-")

        client = self._get_client(
            f"/search/{query}/"
        )  # NOTE: you need to add the trailing slash in here
        query = client.find("div", id="featured")

        # parse search results in here
        data = []
        for i in query.find_all("div", class_="col-md-3 col-xs-6 col-sm-3"):
            data.append(
                {
                    "title": i.find("h2").text.strip(),
                    "link": i.find("a")["href"],
                    "image": i.find("img")["src"],
                }
            )

        return data
