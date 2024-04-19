from crewai import Agent, Task, Crew, Process
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
        allow_delegation=False
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
        tools=tools,  # Este agente pode não precisar de ferramentas específicas para desenvolver o roteiro
        allow_delegation=False
    )


def image_prompt_creator():
    return Agent(
        role='Criador de Prompt de Imagem',
        goal='Desenvolver um prompt detalhado para a criação de uma imagem para o Reels sobre {tema}',
        verbose=True,
        memory=True,
        backstory=(
            "Você é um visionário visual, capaz de imaginar cenas vibrantes e emocionantes com apenas um fechar de olhos. "
            "Sua habilidade em traduzir conceitos e narrativas em imagens impressionantes é o que te destaca. "
            "Você entende o poder de uma imagem em contar uma história e em evocar emoções profundas, "
            "e é exatamente isso que você busca ao criar prompts de imagens detalhados e inspiradores."
        ),
        tools=tools,  # Este agente pode operar sem ferramentas externas, confiando em sua criatividade e conhecimento
        allow_delegation=False
    )


def creative_content_creator():
    return Agent(
        role='Creative Content Creator',
        goal='Develop compelling and innovative content for social media campaigns, with a focus on creating high-impact Instagram ad copies.',
        backstory=(
            "As a Creative Content Creator at a top-tier digital marketing agency, you excel in crafting narratives "
            "that resonate with audiences on social media. Your expertise lies in turning marketing strategies into "
            "engaging stories and visual content that capture attention and inspire action."
        ),
        verbose=True,
        memory=True,  # To remember insights from past research and audience analysis
        tools=tools,  # Assuming there's a tool for analyzing social media trends
        allow_delegation=False
    )
