from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.5
)

prompt = PromptTemplate.from_template(
    """
Generate exactly 5 interview questions about {topic}.

Number them from 1 to 5.
"""

)

chain = prompt | llm

topic = input("Enter subject: ")

result = chain.invoke({
    "topic": topic
})

print("\nINTERVIEW QUESTIONS:")
print(result)