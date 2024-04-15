#pip install crewai
#pip install 'crewai[tools]'
#https://python.langchain.com/docs/integrations/tools/

import os

def get_key(file_path):
    with open(file_path, "rt") as f:
        return f.readline().strip()
    
os.environ["SERPER_API_KEY"] = get_key("c:/src/serperapi.key")
os.environ["OPENAI_API_KEY"] = get_key("c:/src/openai.key")

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

class CrewAiLearn:
    def __init__(self):
        self.search_tool = SerperDevTool()

    def define_agents(self):
        # Creating a senior researcher agent with memory and verbose mode
        self.researcher = Agent(
            role='Senior Researcher',
            goal='Uncover groundbreaking technologies in {topic}',
            verbose=True,
            memory=True,
            backstory=(
            "Driven by curiosity, you're at the forefront of"
            "innovation, eager to explore and share knowledge that could change"
            "the world."
            ),
            tools=[self.search_tool],
            allow_delegation=True
        )

        # Creating a writer agent with custom tools and delegation capability
        self.writer = Agent(
            role='Writer',
            goal='Narrate compelling tech stories about {topic}',
            verbose=True,
            memory=True,
            backstory=(
            "With a flair for simplifying complex topics, you craft"
            "engaging narratives that captivate and educate, bringing new"
            "discoveries to light in an accessible manner."
            ),
            tools=[self.search_tool],
            allow_delegation=False
        )

    def define_tasks(self):
        self.research_task = Task(
            description=(
            "Identify the next big trend in {topic}."
            "Focus on identifying pros and cons and the overall narrative."
            "Your final report should clearly articulate the key points,"
            "its market opportunities, and potential risks."
            ),
            expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
            tools=[self.search_tool],
            agent=self.researcher,
        )

        # Writing task with language model configuration
        self.write_task = Task(
            description=(
            "Compose an insightful article on {topic}."
            "Focus on the latest trends and how it's impacting the industry."
            "This article should be easy to understand, engaging, and positive."
            ),
            expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
            tools=[self.search_tool],
            agent=self.writer,
            async_execution=False,
            output_file='new-blog-post.md'  # Example of output customization
        )


    def assemble_the_crew(self):
        self.crew = Crew(
            agents=[self.researcher, self.writer],
            tasks=[self.research_task, self.write_task],
            process=Process.sequential,  # Optional: Sequential task execution is default
            memory=True,
            cache=True,
            max_rpm=100,
            share_crew=True
        )


    def kick_off(self):
        return self.crew.kickoff(inputs={'topic': 'AI in healthcare'})
      
    def run(self):
        self.define_agents()
        self.define_tasks()
        self.assemble_the_crew()
        return self.kick_off()

print(CrewAiLearn().run())