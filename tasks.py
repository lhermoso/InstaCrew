from crewai import Agent, Task, Crew, Process
# Inicialização das ferramentas que serão usadas pelos agentes
from data import *
from crewai_tools import (
    SerperDevTool, ScrapeElementFromWebsiteTool, PDFSearchTool, DOCXSearchTool,
    GithubSearchTool, CodeDocsSearchTool, WebsiteSearchTool
)

tools = [
    SerperDevTool(),
    ScrapeElementFromWebsiteTool(),
    PDFSearchTool(),
    DOCXSearchTool(),
    GithubSearchTool(content_types=['code'], gh_token='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'),
    CodeDocsSearchTool(),
    WebsiteSearchTool()
]


# Tarefa de pesquisa de tendências
def trend_research_task(agent):
    return Task(
        description=(
            "Investigue as tendências e ideias atuais relacionadas a {tema}. "
            "Concentre-se em curiosidades e temas que podem gerar engajamento "
            "Seu relatório final deve destacar insights e padrões que podem ser utilizados "
            "para criar um Reels com potencial de viralização. Ano atual 2024"
        ),
        expected_output='Um relatório detalhado com insights sobre as tendências atuais e elementos virais no '
                        'Instagram Reels.',
        tools=tools,
        agent=agent,
        memory=True,
        verbose=True
    )


def audience_analysis_task(agent):
    return Task(
        description=(
            "Realize uma análise detalhada da audiência-alvo para o tema {tema}, focando em suas preferências, "
            "comportamentos e interações no Instagram. Utilize essas informações para propor ideias criativas de conteúdo "
            "para Reels que se alinhem com os interesses da audiência e tenham alto potencial de engajamento e viralização."
            "Instagram referencia: https://www.instagram.com/leoohermoso"
        ),
        expected_output=(
            "Sua resposta deve expandir o relatorio recebido uma análise da audiência com detalhes sobre suas preferências e comportamentos, "
            "acompanhado de várias ideias criativas de conteúdo para Reels baseadas nesses insights."
        ),
        tools=tools,
        agent=agent
    )

def viral_idea_selection_task(agent):
    return Task(
        description=(
            "Analise os resultados das pesquisas de tendências e da audiência para selecionar a ideia com o maior potencial de viralização "
            "para o tema {tema}. Avalie as ideias com base em seu potencial de engajamento e relevância para a audiência, identificando "
            "aquela que promete o maior impacto no Instagram Reels."
        ),
        expected_output='A escolha da ideia mais promissora para viralizar no Reels, com uma justificativa detalhada de sua seleção baseada em dados e insights coletados.',
        tools=tools,  # Supondo que o agente já tenha as ferramentas necessárias configuradas
        agent=agent,

    )


def script_development_task(agent):
    return Task(
        description=(
            f"Desenvolva um roteiro detalhado para um Reels que tenha entre 35 e 45 segundos sobre a idea proposta, incorporando as tendências atuais "
            "levantadas nas análises anteriores. O roteiro deve ser estruturado de forma a capturar a atenção imediatamente, "
            "mantendo o engajamento e promovendo a interação do público. Inclua direções claras para filmagem, diálogos, "
            "e qualquer outro elemento relevante que contribua para a narrativa."
            "O reels sera executado por uma unica pessoa, por isso o reels deve focar mais em prender a atencao com um belo titulo, e gancho"
            "A parte de desenvolvimento pode ser eu filmando a tela, ou me filmando, mas nao ha muitos recursos parar editar videos ou"
            "criar efeitos visuais, o roteiro precisa ser possivel de ser executado com poucas ferramentas e rapidamente."
            f"Inspiracoes para Titulos Virais: {titulos}"
            f"Inspiracoes para ganchos Virais: {ganchos}"
            f"Inspiracoes para CTA Virais: {ctas}"
                ""
        ),
        expected_output='Um roteiro detalhado e formatado para produção, incluindo instruções específicas para cada cena'
                        'O Beneficio apenas deve ser introduzido se ele nao for redundante com o Gancho'
                        'Inserir apenas 1 CTA, temos que prender a atencao do expectador, apenas faca o CTA no comeco se o gancho'
                        'for extremamente poderoso'
                        'Estrutura do Roteiro:'
                        '1 - Titulo'
                        '2 - Gancho'
                        '3 - CTA'
                        '4 - Beneficio -> Serve para ancorar o tema do video'
                        '5 - Desenvolvimento'
                        '6 - CTA',
        tools=[],  # Este agente pode operar sem ferramentas externas
        agent=agent,
    )


def image_prompt_task(agent):
    return Task(
    description=(
        "Com base no roteiro desenvolvido, crie um prompt detalhado para a geração de uma imagem que complemente o Reels. "
        "O prompt deve descrever vividamente a cena, incluindo elementos como composição, paleta de cores, emoções a serem transmitidas, "
        "e quaisquer personagens ou objetos específicos que devem ser apresentados. Este prompt será utilizado para instruir a criação "
        "visual, garantindo que a imagem final esteja alinhada com a narrativa e o impacto desejados do Reels."
    ),
    expected_output='Um prompt para IA DALLE detalhado para a criação de uma imagem, incluindo todas as especificações necessárias para garantir que a imagem complemente efetivamente o Reels.',
    tools=[],  # Este agente pode operar sem ferramentas externas
    agent=agent,
)
