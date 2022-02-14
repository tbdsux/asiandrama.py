# asiandrama.py

Asian shows and drama websites scraper library.

## Install

```sh
pip install -m asiandrama
```

## Usage

### Supported Websites

- WatchAsian

  It's website changes everytime so, you need to set a website.

  The website's design and structure could be similar to other ones. This scraper might (should) work also for it.

  - Search drama, show / movies

    ```py
    from asiandrama import WatchAsian

    wa = WatchAsian("https://watchasian.sh")
    search = wa.search("outrun")

    print(search)
    ```

  - Get drama, show / movie page

    ```py
    from asiandrama import WatchAsian

    wa = WatchAsian("https://watchasian.sh")
    drama = wa.fetch_uri("/drama-detail/outrun-by-running-man-2021")
    ```

  - Get drama, show / movie episode page

    ```py
    from asiandrama import WatchAsian

    wa = WatchAsian("https://watchasian.sh")
    ep = wa.get_episode("/outrun-by-running-man-2021-episode-9.html")
    ```

- KShow (`https://kshow123.net/`)

  - Search show

    ```py
    from asiandrama import KShow123

    ks = KShow123()
    ks.search("running")
    ```

  - Get show page

    ```py
    from asiandrama import KShow123

    ks = KShow123()
    show = ks.fetch_uri("/show/running-man-i0/")
    ```

  - Get show episode page

    ```py
    from asiandrama import KShow123

    ks = KShow123()
    ep = ks.get_episode("/show/running-man/episode-587.html")
    ```

##

**2022 | TheBoringDude | [LICENSE](./LICENSE)**
