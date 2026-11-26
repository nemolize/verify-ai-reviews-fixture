# Ground truth for the fixture

Write this down before running any trial, and score each review against it.

The second commit has one defect: `pages += 1` sits inside the retry loop, so `max_pages` counts attempts instead of pages.
A retry therefore uses up the page limit. With `max_pages=2` and a first fetch that times out once, `fetch_all` returns `[1, 2]` instead of `[1, 2, 3, 4]`.

The test added in the second commit passes with the defect, because the default `max_pages=5` leaves room.
