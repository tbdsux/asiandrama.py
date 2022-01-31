from watchasian import WatchAsian


w = WatchAsian("https://watchasian.cc")

q = w.fetch_uri("/drama-detail/outrun-by-running-man-2021")


print(q)
