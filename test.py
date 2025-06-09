from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from third_parties.linkedin_lookup_agent import lookup

if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")

    # sum = """Give me 2 facts about steven speilberg"""
    # sum_temp = PromptTemplate(input_variables=[], template=sum)
    #
    # llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    #
    # chain = sum_temp | llm
    #
    # res = chain.invoke(input={})

    res = lookup("Awais Waheed Confiz")

    print(res)
