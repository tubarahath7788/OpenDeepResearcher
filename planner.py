from langchain_openai import ChatOpenAI
from config.settings import LLM_BASE_URL, LLM_MODEL, OPENAI_API_KEY

def planner_agent(query: str):
    llm = ChatOpenAI(
        base_url=LLM_BASE_URL,
        model=LLM_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0.3
    )

    prompt = f"""
    Break this research topic into 3 sub-questions:
    Topic: {query}
    """

    response = llm.invoke(prompt)
    return response.content

