from crewai import Agent, Task, Crew, Process

from agents import *
from tasks import *

# Inicializando as ferramentas que serão usadas pelos agentes

print("## Bem-vindo ao criador de reels virais")
print('-------------------------------')
tema = input("Qual tema vamos gerar o reels\n")

# Definindo os agentes
trend_researcher_agent = trend_researcher()
audience_analyst_agent = audience_analyst()
script_developer_agent = script_developer()
senior_photographer = senior_photographer_agent()
chief_creative_diretor = chief_creative_diretor_agent()

# Definindo as tarefas
trend_research_task_instance = trend_research_task(trend_researcher_agent)
trend_research_task_social_instance = trend_research_task_social(trend_researcher_agent)
audience_analysis_task_instance = audience_analysis_task(audience_analyst_agent)
script_development_task_instance = script_development_task(script_developer_agent,
                                                           context=[trend_research_task_instance,
                                                                    trend_research_task_social_instance])
take_photo = take_photograph_task(senior_photographer)
approve_photo = review_photo(chief_creative_diretor)

# Configurando a tripulação (Crew) e o processo de execução das tarefas
crew = Crew(
    agents=[
        trend_researcher_agent,
        audience_analyst_agent,
        script_developer_agent,
    ],
    tasks=[
        trend_research_task_instance,
        trend_research_task_social_instance,
        audience_analysis_task_instance,
        script_development_task_instance,

    ],
    memory=True,
    process=Process.sequential,
    verbose=True
)

image_crew = Crew(
    agents=[
        senior_photographer,
        chief_creative_diretor
    ],
    tasks=[
        take_photo,
        approve_photo
    ],
    verbose=True
)

# Iniciando a execução das tarefas pela tripulação
ad_copy = crew.kickoff(inputs={'tema': tema})

image = image_crew.kickoff(
    inputs={"copy": ad_copy, "tema": tema})

# Imprimindo o resultado das tarefas
print("Roteiro do reels")
print(ad_copy)
print("'\n\nDescricao da Imagem:")
print(image)
