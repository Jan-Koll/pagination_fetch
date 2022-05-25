import pagination_fetch
url = "https://example.com/api/users"
min_page, max_page = 1, 10
results = pagination_fetch.fetch_paginate(url, min_page, max_page)
pagination_fetch.exportToJson(results)