# Inicialização das ferramentas que serão usadas pelos agentes
import os
from textwrap import dedent

from crewai import Task
from crewai_tools import (
    SerperDevTool, ScrapeElementFromWebsiteTool, PDFSearchTool, DOCXSearchTool,
    GithubSearchTool, CodeDocsSearchTool, WebsiteSearchTool
)
from dotenv import load_dotenv

load_dotenv()
tools = [
    SerperDevTool(),
    ScrapeElementFromWebsiteTool(),
    PDFSearchTool(),
    DOCXSearchTool(),
    GithubSearchTool(content_types=['code'], gh_token=os.getenv('GH_TOKEN')),
    CodeDocsSearchTool(),
    WebsiteSearchTool()
]


# Tarefa de pesquisa de tendências
def trend_research_task(agent):
    return Task(
        description=(
            "Realize uma pesquisa abrangente na internet para coletar fatos e tendências sobre {tema}. "
            "Examine diversas fontes para entender as discussões atuais, desenvolvimentos, "
            "e as perspectivas emergentes relacionadas a esse tema. "
            "Seu objetivo é identificar informações chave que destaquem as tendências predominantes, "
            "os pontos de vista principais e quaisquer dados estatísticos ou estudos recentes associados ao tema."
        ),
        expected_output='Um relatório compreensivo detalhando os fatos encontrados e as tendências identificadas '
                        'sobre o tema {tema}, incluindo uma análise dos dados e perspectivas coletadas de várias fontes.',
        tools=tools,
        agent=agent,
        memory=True,
        verbose=True
    )


def trend_research_task_social(agent):
    return Task(
        description=(
            "Investigue tendências específicas nas mídias sociais relacionadas ao tema {tema}, com foco em aplicação no Instagram Reels. "
            "Examine plataformas populares como TikTok, YouTube Shorts e outros, para identificar elementos como conteúdo viral, "
            "hashtags relevantes e técnicas de storytelling que estão em alta. "
            "Avalie como esses elementos podem ser adaptados ou inspirar a criação de Reels no Instagram que se conectem efetivamente ao público interessado no tema {tema}."
        ),
        expected_output='Um relatório detalhado que descreve tendências emergentes nas mídias sociais específicas ao tema {tema}, '
                        'incluindo recomendações sobre como essas tendências podem ser transformadas em conteúdo viral no Instagram Reels.',
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
            "Instagram referencia: https://instagram.com/leoohermoso"
        ),
        expected_output=(
            "Sua resposta deve expandir o relatorio recebido uma análise da audiência com detalhes sobre suas preferências e comportamentos, "
            "acompanhado de várias ideias criativas de conteúdo para Reels baseadas nesses insights."
        ),
        tools=tools,
        agent=agent
    )


def script_development_task(agent,context):
    return Task(
        description=(
            "Desenvolva um roteiro detalhado para um Reels sobre o tema {tema}, incorporando as tendências atuais e as ideias criativas "
            "levantadas nas análises anteriores. O roteiro deve ser estruturado de forma a capturar a atenção imediatamente, "
            "mantendo o engajamento e promovendo a interação do público. Inclua direções claras para filmagem, diálogos, "
            "e qualquer outro elemento relevante que contribua para a narrativa."
        ),
        expected_output='Um roteiro detalhado e formatado para produção, incluindo instruções específicas para cada cena, diálogos e chamadas para ação.',
        tools=tools,  # Este agente pode operar sem ferramentas externas
        agent=agent,
        context=context
    )


def take_photograph_task(agent):
    return Task(description=dedent("""\
        Você está trabalhando em uma nova campanha para um cliente super importante,
        e você DEVE tirar a foto mais incrível de todas para uma postagem no Instagram
        sobre o tema, você tem a seguinte cópia:
        
        {copy}

        Este é o tema com o qual você está trabalhando: {tema}.

        Imagine qual foto você quer tirar e descreva-a em um parágrafo.
        Aqui estão alguns exemplos para você seguir:
        - um avião de alta tecnologia em um belo céu azul em um lindo pôr do sol super nítido belo em 4k, tomada ampla profissional
        - a última ceia, com Jesus e seus discípulos, partindo o pão, tomada próxima, iluminação suave, 4k, nítida
        - um homem barbudo nas neves, usando roupas muito quentes, com montanhas cobertas de neve ao fundo, iluminação suave, 4k, nítido, close na câmera

        Pense de forma criativa e concentre-se em como a imagem pode capturar a atenção do público.
        Não mostre o produto real na foto.

        """),
                expected_output="""Sua resposta final deve ser 3 opções de fotografias, cada uma com 1 parágrafo
        descrevendo a fotografia exatamente como os exemplos fornecidos acima.""",
                tools=tools,  # Este agente pode operar sem ferramentas externas
                agent=agent,
                verbose=True
                )


def review_photo(agent):
    return Task(description=dedent("""\
        Revise as fotos que você recebeu do fotógrafo sênior.
        Certifique-se de que estão as melhores possíveis e alinhadas com os objetivos do produto,
        revise, aprove, faça perguntas esclarecedoras ou delegue trabalho adicional se
        necessário para tomar decisões. Ao delegar trabalho, envie o rascunho completo
        como parte das informações.

        Este é o tema com o qual você está trabalhando: tema.
        Copy do post: {copy}

        Aqui estão alguns exemplos de como as fotografias finais devem parecer:
        - um avião de alta tecnologia em um belo céu azul em um lindo pôr do sol super nítido belo em 4k, tomada ampla profissional
        - a última ceia, com Jesus e seus discípulos, partindo o pão, tomada próxima, iluminação suave, 4k, nítida
        - um homem barbudo nas neves, usando roupas muito quentes, com montanhas cobertas de neve ao fundo, iluminação suave, 4k, nítido, close na câmera
        """),
                expected_output="""
        Sua resposta final deve ser 3 opções revisadas de fotografias,
        cada uma com 1 parágrafo de descrição seguindo os exemplos fornecidos acima.""",

                agent=agent,
                tools=tools,
                verbose=True
                )
