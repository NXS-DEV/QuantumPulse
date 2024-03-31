from crewai import Agent
from crewai_tools import SerperDevTool
from crewai import Task
search_tool = SerperDevTool()


# Creating the agent designer
ai_designer = Agent(
    role='designer',
    goal='Create innovative and aesthetically pleasing user interfaces.',
    verbose=True,
    memory=True,
    backstory=(),
    tools=[search_tool],
    allow_delegation=True
)
# you can create others agent in the same file.

# Define the task for the ai designer
create_and_report =Task(
    description=(
"Identify the next big trend in user interface design."
"Focus on analyzing emerging design methodologies and technologies, considering their compatibility with the goal of creating innovative and aesthetically pleasing interfaces."
"Your final report should clearly articulate the key points regarding its market opportunities, potential risks, and how these trends align with the capabilities of the AI designer agent, including its tools and delegation capabilities."
    ),
    expected_output='A comprehensive report detailing the identified trend, its implications for interface design, market opportunities, potential risks, and how it aligns with the capabilities of the AI designer agent. This report should provide actionable insights for leveraging the trend to enhance the agent\'s design process.',
    tools=[search_tool],
    agent=ai_designer,
    async_execution=False,
    output_file='.pdf'  # Example of output customization
)
# code need to be fixed and add discord.py for discord.client.


