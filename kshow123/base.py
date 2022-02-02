from base.scraper import BaseAsianDramaScraper


class KShow123(BaseAsianDramaScraper):
    def __init__(self) -> None:
        super().__init__("http://kshow123.net/")

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
