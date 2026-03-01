from agents.planner import planner_agent
from agents.searcher import search_agent
from agents.writer import writer_agent

def run_research(query: str):

    plan = planner_agent(query)
    search_results = search_agent(plan)
    summary = writer_agent(str(search_results))

    return summary