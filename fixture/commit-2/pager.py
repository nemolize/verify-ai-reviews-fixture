def fetch_all(fetch, first_url, max_pages=5, retries=2):
    items, url, pages = [], first_url, 0
    while url and pages < max_pages:
        for attempt in range(retries + 1):
            pages += 1
            try:
                page = fetch(url)
                break
            except TimeoutError:
                if attempt == retries:
                    raise
        items.extend(page["items"])
        url = page.get("next")
    return items
