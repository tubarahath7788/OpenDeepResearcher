from tavily import TavilyClient
from config.settings import TAVILY_API_KEY

def searcher_agent(query: str):
    client = TavilyClient(api_key=TAVILY_API_KEY)

    response = client.search(
        query=query,
        search_depth="basic",
        max_results=3
    )

    results = []

    for result in response["results"]:
        results.append(f"Title: {result['title']}\nURL: {result['url']}\n")

    return "\n".join(results)
