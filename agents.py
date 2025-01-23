from crewai import Agent, LLM
from tools import yt_tool

from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
llm = os.getenv("OPENAI_MODEL_NAME")


# Create a blog content researcher
blog_researcher = Agent(
    role = "Blog Researcher from Youtube videos",
    goal = "Get the relevant video content for the topic : {topic} from YT Channel",
    verbose = True,
    memory = True,
    backstory =(
        "Expert in understanding videos in AI, Data Science, Machine Learning and Gen AI and provide suggestion"
    ),
    tools =[yt_tool],
    llm=LLM(model="ollama/deepseek-r1:8b", base_url="http://localhost:11434"),
    allow_delegation = True
)

#creating a blog writer agent with YT tool

blog_writer = Agent(
    role = "Blog Writer",
    goal = "Write compelling tech stories about the video : {topic}  from YT channel.",
    verbose = True,
    memory = True,
    backstory =(
        "With a flair for simplifying complex topics, you craft"
        "engage narratives that captivate and educate, brining new"
        "discoveries to light in an accessible manner."
    ),
    tools =[yt_tool],
    llm=LLM(model="ollama/deepseek-r1:8b", base_url="http://localhost:11434"),
    allow_delegation = False
)
