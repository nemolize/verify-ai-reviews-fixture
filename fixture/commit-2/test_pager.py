from pager import fetch_all

PAGES = {
    "p1": {"items": [1, 2], "next": "p2"},
    "p2": {"items": [3, 4], "next": "p3"},
    "p3": {"items": [5], "next": None},
}


def test_collects_every_page():
    assert fetch_all(PAGES.__getitem__, "p1") == [1, 2, 3, 4, 5]


def test_stops_at_max_pages():
    assert fetch_all(PAGES.__getitem__, "p1", max_pages=2) == [1, 2, 3, 4]


def test_retries_a_timeout_once():
    calls = []

    def flaky(url):
        calls.append(url)
        if len(calls) == 1:
            raise TimeoutError
        return PAGES[url]

    assert fetch_all(flaky, "p1") == [1, 2, 3, 4, 5]
