""" 
Basic example of scraping pipeline using SmartScraper
"""

import os, json
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperMultiGraph

load_dotenv()

# ************************************************
# Define the configuration for the graph
# ************************************************

openai_key = os.getenv("OPENAI_APIKEY")

graph_config = {
    "llm": {
        "api_key": openai_key,
        "model": "gpt-4o",
    },
    "verbose": True,
    "headless": False,
}

# *******************************************************
# Create the SmartScraperMultiGraph instance and run it
# *******************************************************

multiple_search_graph = SmartScraperMultiGraph(
    prompt="Who is Marco Perini?",
    source= [
        "https://perinim.github.io/",
        "https://perinim.github.io/cv/"
        ],
    schema=None,
    config=graph_config
)

result = multiple_search_graph.run()
print(json.dumps(result, indent=4))
