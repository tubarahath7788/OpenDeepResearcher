from graph.workflow import run_research

if __name__ == "__main__":
    query = input("Enter research topic: ")
    result = run_research(query)
    print("\nFinal Research Summary:\n")
    print(result)