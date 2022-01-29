from smaxpy import Smax
from urllib.parse import urljoin


class WatchAsian:
    def __init__(self, website: str):
        self.__website = website

    def search(self, query: str):
        client = Smax(urljoin(self.__website, f"search?type=movies&keyword={query}"))

        query = client.find("div", class_="block tab-container")

        data = []
        for i in query.find_all("li"):
            link = i.find("a")["href"]
            image = i.find("img")["data-original"]
            title = i.find("h3").text.strip()

            data.append(
                {"link": urljoin(self.__website, link), "image": image, "title": title}
            )

        return data
