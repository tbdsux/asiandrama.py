class ScrapedResponse:
    def json(self):
        """Sub class should implement this function."""

    def __repr__(self) -> str:
        return str(self.json())
