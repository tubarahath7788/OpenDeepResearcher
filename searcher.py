from tavily import TavilyClient
from config.settings import TAVILY_API_KEY


def search_agent(query: str):
    client = TavilyClient(api_key=TAVILY_API_KEY)

    results = client.search(
        query=query,
        max_results=3
    )

    return results