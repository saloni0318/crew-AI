from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=False,
  cache=False,
  max_rpm=5,
  share_crew=True
)
 
## start the task execution process with enhanced feedback
# result=crew.kickoff(inputs={'topic':'AI VS ML VS DL vs Data Science'})
result = crew.kickoff(inputs={
    'topic': 'AI VS ML VS DL vs Data Science',
    'youtube_channel_handle': '@krishnaik06'  # Pass the handle here
})
print(result)