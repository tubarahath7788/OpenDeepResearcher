from langchain.chat_models import ChatOpenAI
from config.settings import LLM_BASE_URL, LLM_MODEL


def writer_agent(content: str):
    llm = ChatOpenAI(
        base_url=LLM_BASE_URL,
        model=LLM_MODEL,
        temperature=0.5
    )

    prompt = f"""
    Summarize the following research content clearly and concisely:

    {content}
    """

    response = llm.invoke(prompt)
    return response.content