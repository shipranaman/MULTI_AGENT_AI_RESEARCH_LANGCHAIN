from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain,
)


def run_research_pipeline(topic: str) -> dict:
    state = {}

    # =========================
    # Step 1 - Search Agent
    # =========================
    print("\n" + "=" * 50)
    print("Step 1 - Search Agent is working...")
    print("=" * 50)

    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            (
                "user",
                f"""
Search the web for: {topic}

IMPORTANT INSTRUCTIONS:
1. Use the web_search tool.
2. Return ALL search results exactly as returned by the tool.
3. DO NOT summarize.
4. DO NOT explain.
5. DO NOT remove any URL.
6. Show Title, URL and Snippet for every result.

Return only the search results.
"""
            )
        ]
    })

    state["search_results"] = search_result["messages"][-1].content

    print("\nSearch Results:\n")
    print(state["search_results"])

    # =========================
    # Step 2 - Reader Agent
    # =========================
    print("\n" + "=" * 50)
    print("Step 2 - Reader Agent is scraping top resources...")
    print("=" * 50)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"""
Below are the search results.

{state['search_results']}

Choose the MOST relevant URL.

Use the scrape_url tool on that URL.

Return ONLY the scraped content.
"""
            )
        ]
    })

    state["scraped_content"] = reader_result["messages"][-1].content

    print("\nScraped Content:\n")
    print(state["scraped_content"])

    # =========================
    # Step 3 - Writer
    # =========================
    print("\n" + "=" * 50)
    print("Step 3 - Writer is drafting the report...")
    print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS:\n\n{state['search_results']}\n\n"
        f"SCRAPED CONTENT:\n\n{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\nFinal Report:\n")
    print(state["report"])

    # =========================
    # Step 4 - Critic
    # =========================
    print("\n" + "=" * 50)
    print("Step 4 - Critic is reviewing the report...")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\nCritic Feedback:\n")
    print(state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("\nEnter a research topic: ")
    run_research_pipeline(topic)