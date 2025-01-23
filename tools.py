from crewai_tools import YoutubeChannelSearchTool
import os
from dotenv import load_dotenv
load_dotenv()

youtube_channel_handle = os.getenv("YOUTUBE_CHANNEL_HANDLE")

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle= youtube_channel_handle)