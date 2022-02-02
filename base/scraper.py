from urllib.parse import urljoin

from smaxpy import Smax


class BaseAsianDramaScraper:
    def __init__(self, website: str) -> None:
        self.website = website

    def _get_client(self, url: str) -> Smax:
        """
        Create new Smax client.
        """

        return Smax(urljoin(self.website, url))
