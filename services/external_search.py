from duckduckgo_search import ddg

def search_product_online(query):
    results = ddg(query, max_results=3)
    return [res["title"] + " - " + res["href"] for res in results]
