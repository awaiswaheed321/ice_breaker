from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

info = """
Steven Allan Spielberg (/ˈspiːlbɜːrɡ/ SPEEL-burg; born December 18, 1946) is an American filmmaker. A major figure of the New Hollywood era and pioneer of the modern blockbuster, Spielberg is widely regarded as one of the greatest film directors of all time and is the highest-grossing film director of all time.[1] Several of Spielberg's works are considered among the greatest films in history, and some are among the highest-grossing films ever.[2]

Spielberg was born in Cincinnati, Ohio, and grew up in Phoenix, Arizona.[3] He moved to California and studied film in college. After directing several episodes for television, including Night Gallery and Columbo, he directed the television film Duel (1971), which was approved by Barry Diller. He made his theatrical debut with The Sugarland Express (1974) and became a household name with the summer blockbuster Jaws (1975). He directed more escapist box office successes with Close Encounters of the Third Kind (1977), E.T. the Extra-Terrestrial (1982) and the original Indiana Jones trilogy (1981–1989). He explored drama in The Color Purple (1985) and Empire of the Sun (1987).

In 1993, Spielberg directed back-to-back hits with the science fiction thriller Jurassic Park, the highest-grossing film ever at the time, and the epic historical drama Schindler's List, which has often been listed as one of the greatest films ever made. He won the Academy Award for Best Director for the latter as well as for the World War II epic Saving Private Ryan (1998). Spielberg has since directed the science fiction films A.I. Artificial Intelligence (2001), Minority Report (2002), War of the Worlds (2005) and Ready Player One (2018); the historical dramas Amistad (1997), Munich (2005), War Horse (2011), Lincoln (2012), Bridge of Spies (2015) and The Post (2017); the comedies Catch Me If You Can (2002) and The Terminal (2004); the animated film The Adventures of Tintin (2011); the musical West Side Story (2021); and the family drama The Fabelmans (2022).
"""

if __name__ == '__main__':
    print("App Started")

    summary_template = """
        given the info {info} of a person, give 2 pieces of info about them.
    """

    summary_prompt_template = PromptTemplate(input_variables=["info"],template=summary_template)

    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser
    res = chain.invoke(input={"info": info})

    print(res)

