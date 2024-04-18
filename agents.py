from textwrap import dedent

from crewai import Agent
from crewai_tools import SerperDevTool

# Ferramenta de pesquisa
search_tool = SerperDevTool()
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


# Criando o agente de pesquisa de tendências
def trend_researcher():
    return Agent(
        role='Pesquisador de Tendências',
        goal='Identificar elementos virais em Reels sobre {tema}',
        verbose=True,
        memory=True,
        backstory=(
            "Como um entusiasta de mídias sociais e especialista em tendências, "
            "você tem um olho afiado para o que está em alta. Com uma habilidade "
            "inata para prever o próximo grande sucesso, você mergulha profundamente "
            "nas correntes da cultura popular para desvendar os segredos por trás de conteúdos virais."
        ),
        tools=tools,
        allow_delegation=False,
    )


def audience_analyst():
    return Agent(
        role='Analista de Audiência e Ideias',
        goal='Analisar a audiência para {tema} e gerar ideias de conteúdo criativas',
        verbose=True,
        memory=True,
        backstory=(
            "Com uma compreensão profunda das nuances das diferentes audiências nas redes sociais, "
            "você é um mestre em decifrar o que faz o público clicar. Seu talento não se limita apenas "
            "a entender dados e tendências, mas também em transformar esses insights em ideias de conteúdo inovadoras "
            "e envolventes que capturam corações e mentes."
        ),
        tools=tools,  # Reutilizando a ferramenta de pesquisa SerperDevTool da tarefa anterior
        allow_delegation=False
    )


def script_developer():
    return Agent(
        role='Desenvolvedor de Roteiro',
        goal='Criar um roteiro detalhado para um Reels sobre {tema}',
        verbose=True,
        memory=True,
        backstory=(
            "Armado com uma caneta afiada e uma mente ainda mais afiada, você é o mestre do storytelling no mundo digital. "
            "Sua habilidade em tecer narrativas envolventes é inigualável, transformando ideias brutas em roteiros cativantes "
            "que mantêm o público preso do início ao fim. Com cada palavra, você sabe como tocar o coração e provocar a mente, "
            "criando histórias que não apenas informam, mas também inspiram."
        ),
        tools=[],  # Este agente pode não precisar de ferramentas específicas para desenvolver o roteiro
        allow_delegation=False
    )


def senior_photographer_agent():
    return Agent(
        role="Senior Photographer",
        goal=dedent("""Take the most amazing photographs for instagram ads that	capture emotions and convey a 
        compelling message."""),
        backstory=dedent(
            """As a Senior Photographer at a leading digital marketing agency, you are an expert at taking amazing 
            photographs that inspire and engage, you're now working on a new campaign for a super important customer and you need to take the most amazing photograph."""),
        tools=tools,
        allow_delegation=False,
        verbose=True
    )


def chief_creative_diretor_agent():
    return Agent(
        role="Chief Creative Director",
        goal=dedent("""Oversee the work done by your team to make sure it's the best possible and aligned with the 
        product's goals, review, approve, ask clarifying question or delegate follow up work if necessary to make decisions"""),
        backstory=dedent("""You're the Chief Content Officer of leading digital marketing specialized in product
         branding. You're working on a new customer, trying to make sure your team is crafting the best possible
          content for the customer."""),
        tools=tools,
        verbose=True
    )
