import os
from crewai import Agent, Task, Crew, Process
from textwrap import dedent

# Configurar as chaves de API necessárias
from crewai_tools import (
    SerperDevTool, ScrapeElementFromWebsiteTool, PDFSearchTool, DOCXSearchTool,
    GithubSearchTool, CodeDocsSearchTool, WebsiteSearchTool, YoutubeVideoSearchTool
)
from langchain_openai import ChatOpenAI

# Inicializar a ferramenta de pesquisa
llm_writer = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0.9, max_retries=100)
llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0.5, max_retries=100)

# Inicialização das ferramentas que serão usadas pelos agentes
tools = [
    SerperDevTool(),
    ScrapeElementFromWebsiteTool(),
    PDFSearchTool(),
    DOCXSearchTool(),
    CodeDocsSearchTool(),
    WebsiteSearchTool(),
    YoutubeVideoSearchTool(),
]
# Agente de Pesquisa Universal
# Agente de Pesquisa Universal: Alex, o Explorador de Informações
researcher = Agent(
    role='Explorador de Informações',
    goal='Navegar pelo vasto oceano da internet para coletar tesouros de conhecimento sobre qualquer tópico fornecido.',
    tools=tools,
    verbose=True,
    memory=True,
    allow_delegation=True,
    backstory=(
        "Alex sempre foi fascinado pelo desconhecido. Desde pequeno, passava horas lendo enciclopédias e navegando"
        " na web em busca de aprender tudo sobre tudo. Agora, como um Explorador de Informações, Alex utiliza sua"
        " curiosidade insaciável e habilidades de pesquisa para descobrir insights profundos e informações valiosas"
        " sobre os mais diversos tópicos, transformando complexidade em simplicidade."
    )
)

# Agente Redator de Conteúdo: Luna, a Contadora de Histórias
writer = Agent(
    role='Contadora de Histórias',
    goal='Tecer narrativas envolventes que capturam a essência de um tópico, educando e entretendo o público.',
    verbose=True,
    memory=True,
    tools=tools,
    allow_delegation=False,
    backstory=(
        "Luna cresceu em meio a livros e histórias fantásticas, o que moldou sua paixão por contar histórias. Ela"
        " tem o dom de dar vida a qualquer tópico com sua escrita cativante, transformando informações brutas em"
        " roteiros de post envolventes que falam diretamente ao coração dos leitores, encorajando-os a explorar"
        " novos horizontes."
    )
)

# Agente de Otimização e Viralização: Max, o Estrategista Viral
optimizer = Agent(
    role='Estrategista Viral',
    goal='Refinar o conteúdo para maximizar seu engajamento e potencial de compartilhamento, garantindo que cada post seja uma semente para virais.',
    verbose=True,
    memory=True,
    allow_delegation=False,
    tools=tools,
    backstory=(
        "Max é um mestre da psicologia das mídias sociais e um ávido estudante das tendências da internet. Com um"
        " olho afiado para o que faz o conteúdo clicar com o público, Max ajusta cada roteiro para garantir que ele"
        " não só chame a atenção, mas também incite a ação, transformando simples posts em fenômenos virais."
    )
)

# Definição das Tarefas
# Tarefa de Pesquisa: A Grande Busca de Alex
research_task = Task(
    description=(
        "Em uma jornada digital através dos confins da internet, Alex irá mergulhar em fontes variadas, desde"
        " artigos acadêmicos até fóruns de nicho, para coletar informações valiosas e insights sobre o tópico '{input}'."
        " Sua missão é trazer à tona conhecimentos que não só sejam relevantes e atuais, mas que também ofereçam uma"
        " nova perspectiva sobre o assunto."
        ""
        "Meu instagram: https://instagram.com/leoohermoso"
    ),
    expected_output=(
        "Uma compilação de informações, dados e insights relevantes sobre o tópico, organizada de forma clara e"
        " acessível."
    ),
    agent=researcher,
    # Outras configurações conforme necessário
)

# Tarefa de Redação: O Mosaico de Palavras de Luna
writing_task = Task(
    description=(
        "Com a tapeçaria de informações tecida por Alex em mãos, Luna começará sua arte. Ela irá compor um roteiro"
        " onde cada parágrafo é uma pincelada, cada frase uma cor, dando vida a um post que não apenas informa, mas"
        " encanta. O roteiro iniciará com um gancho irresistível, seguido por um conteúdo rico que ilumina o tópico"
        " '{input}' sob uma nova luz, culminando em um CTA poderoso que convida à ação, sem esquecer de um fechamento"
        " que ressoa e perdura na mente do leitor."
    ),
    expected_output=(
        "Um roteiro detalhado para um reels, incluindo um gancho de abertura, desenvolvimento do conteúdo, um CTA claro"
        " e um fechamento memorável."
    ),
    agent=writer,
    # Outras configurações conforme necessário
)

# Tarefa de Otimização: O Toque de Midas de Max
optimization_task = Task(
    description=(
        "Max recebe o roteiro nascente de Luna e, com seu toque de Midas, começa a transformação. Ele analisará cada"
        " elemento, ajustando, refinando e polindo para garantir que o post não só capture a atenção, mas também acenda"
        " a chama do engajamento. Max estará atento às tendências virais, incorporando-as de forma sutil, garantindo que"
        " cada palavra tenha o potencial de ser ecoada através do vasto mundo das mídias sociais."
    ),
    expected_output=(
        "O roteiro final otimizado para viralizacao, incluindo ajustes para aumentar a relevância, dicas de hashtags"
        " populares, e estratégias para encorajar interações, pronto para capturar corações e mentes no Instagram."
    ),
    agent=optimizer,
    # Outras configurações conforme necessário
)

# Configuração do Crew
crew = Crew(
    agents=[researcher, writer, optimizer],
    tasks=[research_task, writing_task, optimization_task],
    process=Process.sequential,  # Execução sequencial das tarefas,
    verbose=True,
    memory=True
)

# Executar o Crew
result = crew.kickoff(inputs={'input': 'Por que estou comprando KASPA'})
print(result)
