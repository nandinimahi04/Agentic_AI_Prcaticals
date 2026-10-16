from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.2
)

prompt = PromptTemplate.from_template(
    """
Translate the following English text into {language}.

Text:
{text}

Return only the translated text.
"""
)

chain = prompt | llm

text = input("Text: ")
language = input("Language: ")

print(
    chain.invoke({
        "text": text,
        "language": language
    })
)