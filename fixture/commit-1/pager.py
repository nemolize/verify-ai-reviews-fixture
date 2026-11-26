def fetch_all(fetch, first_url, max_pages=5):
    items, url, pages = [], first_url, 0
    while url and pages < max_pages:
        page = fetch(url)
        items.extend(page["items"])
        url = page.get("next")
        pages += 1
    return items
