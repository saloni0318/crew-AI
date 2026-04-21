import os
os.environ["LITELLM_RETRY_STRATEGY"] = "exponential_backoff_retry"

from crewai import Agent, LLM
from tools import yt_tool

openrouter_llm = LLM(
    # LiteLLM needs 'openrouter/' prefix for the model
    model="openrouter/minimax/minimax-m2.5:free", 
    # Use the /v1 suffix
    base_url="https://openrouter.ai/api/v1",
    # Ensure your .env variable matches this key
    api_key=os.getenv("OPENROUTER_API_KEY"),
    # Adding this helps stabilize OpenRouter calls
    temperature=0.7
)


## Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the channel {youtube_channel_handle}',
    verbose=True,
    memory=False,
    backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools=[yt_tool],
    llm=openrouter_llm, 
    allow_delegation=False
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=False, 
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=openrouter_llm, 
    allow_delegation=False


)