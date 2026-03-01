from langchain.chat_models import ChatOpenAI
from config.settings import LLM_BASE_URL, LLM_MODEL


def planner_agent(query: str):
    llm = ChatOpenAI(
        base_url=LLM_BASE_URL,
        model=LLM_MODEL,
        temperature=0.3
    )

    prompt = f"""
    Break this research topic into 3 clear sub-questions:
    Topic: {query}
    """

    response = llm.invoke(prompt)
    return response.content
