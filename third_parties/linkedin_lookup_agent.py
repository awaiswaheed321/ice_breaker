import os
from dotenv import load_dotenv

from tools.tools import get_profile_url

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    template = """given full name {name_of_person} i want you to get me a link to their profile page. 
        Your answer should only contain a URL."""

    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Linkedin profile page",
            func=get_profile_url,
            description="useful for when you need to get the Linkedin profile URL"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": prompt_template.format_prompt(name_of_person=name)})
    linkedin_profile_url = result["output"]
    return linkedin_profile_url