from crewai import Agent, Task, Crew, Process

from agents import *
from tasks import *

# Inicializando as ferramentas que serão usadas pelos agentes


# Definindo os agentes
trend_researcher_agent = trend_researcher()
audience_analyst_agent = audience_analyst()
creative_content_creator_agent = creative_content_creator()
script_developer_agent = script_developer()
image_prompt_creator_agent = image_prompt_creator()

# Definindo as tarefas
trend_research_task_instance = trend_research_task(trend_researcher_agent)
audience_analysis_task_instance = audience_analysis_task(audience_analyst_agent)
viral_idea_selection_task_instance = viral_idea_selection_task(creative_content_creator_agent)
script_development_task_instance = script_development_task(script_developer_agent)
image_prompt_task_instance = image_prompt_task(image_prompt_creator_agent)

# Configurando a tripulação (Crew) e o processo de execução das tarefas
crew = Crew(
    agents=[
        trend_researcher_agent,
        audience_analyst_agent,
        creative_content_creator_agent,
        script_developer_agent,
        image_prompt_creator_agent
    ],
    tasks=[
        trend_research_task_instance,
        audience_analysis_task_instance,
        viral_idea_selection_task_instance,
        script_development_task_instance,
        image_prompt_task_instance
    ],
    memory=True,
    process=Process.sequential  # Execução sequencial das tarefas
)
tema = input("Quer Viralizar o que?")
# Iniciando a execução das tarefas pela tripulação
result = crew.kickoff(inputs={'tema': tema})

result = script_development_task_instance.output.exported_output + "\n\n" + result

# Imprimindo o resultado das tarefas
print(result)
