from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

#Research Task
research_task = Task(
    description=(
        "Identify the video {topic}."
        "Get detailed information about the video from the channel"

    ),
    expected_output="A comprehensive 3 paragraphs long report based on the {topic} of the video content",
    tools=[yt_tool],
    agent=blog_researcher,
)

#writing task with language model configuration
write_task = Task(
    description=(
        "Get infor from the youtuve channel on topic {topic}"
    ),
    expected_output="Summarize the info from the youtube channel video on the topic {topic} and create content for the blog ",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="blog_content.md"
)