from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(
    model="llama3.2",
    temperature=0
)

prompt = PromptTemplate.from_template(
    """
Extract exactly 5 important keywords from the following text.

Return only the keywords.

Text:
{text}
"""
)

chain = prompt | llm

text = input("Enter text: ")

print("\nKEYWORDS:")

print(
    chain.invoke({
        "text": text
    })
)