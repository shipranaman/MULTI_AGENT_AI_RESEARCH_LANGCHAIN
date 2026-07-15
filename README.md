# Multi-Agent AI Research System with LangChain

## Project Overview

This project is an AI-powered Multi-Agent Research System that automates end-to-end web research using specialized AI agents. Instead of relying on a single LLM response, the system follows a structured multi-agent workflow where each agent performs a dedicated task such as searching the web, extracting webpage content, generating research reports, and reviewing the final output.

The application is built using LangChain, LangGraph, Google Gemini, Tavily Search API, BeautifulSoup, and Streamlit.

---

## Features

- Multi-Agent architecture using LangGraph
- AI-powered Search Agent
- Reader Agent for webpage understanding
- Live web search using Tavily Search API
- Web scraping using BeautifulSoup
- Writer Chain for structured report generation
- Critic Chain for response validation
- Source-aware research reports
- Interactive Streamlit interface
- Modular and extensible architecture

---

## Research Workflow

```
User Research Query
        │
        ▼
 Search Agent
        │
        ▼
 Tavily Search API
        │
        ▼
 Reader Agent
        │
        ▼
 BeautifulSoup Web Scraper
        │
        ▼
 Writer Chain
        │
        ▼
 Critic Chain
        │
        ▼
 Final Research Report
```


## Technologies Used

### AI Frameworks

- LangChain

### Large Language Model

- MISTRAL.AI

### Search

- Tavily Search API

### Web Scraping

- BeautifulSoup
- Requests

### Frontend

- Streamlit

### Programming Language

- Python

---

## Workflow Components

### Search Agent

Performs intelligent web searches using Tavily Search API and retrieves the most relevant webpages based on the user's research query.

### Reader Agent

Visits the retrieved webpages and extracts useful content using BeautifulSoup for further analysis.

### Writer Chain

Processes the collected information and generates a structured research report.

### Critic Chain

Reviews the generated report, validates the quality of the response, and improves the final output before presenting it to the user.

---

## Skills Demonstrated

- Multi-Agent Systems
- LangGraph State Management
- LangChain Agents
- AI Workflow Orchestration
- Prompt Engineering
- Google Gemini Integration
- Tavily API Integration
- Web Scraping
- Python Development
- Streamlit Application Development

