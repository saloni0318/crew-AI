from dotenv import load_dotenv
import os

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY")
if openai_key:
    os.environ["OPENAI_API_KEY"] = openai_key
    if not os.getenv("OPENAI_API_BASE") and os.getenv("OPENROUTER_API_KEY"):
        os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/v1"
else:
    raise RuntimeError(
        "OpenAI API key not found. Set OPENAI_API_KEY or OPENROUTER_API_KEY in your .env file."
    ) 

from crewai_tools import YoutubeChannelSearchTool

# Correct usage: Pass ONLY the handle string
# yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')
yt_tool = YoutubeChannelSearchTool() 
