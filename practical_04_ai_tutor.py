from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.4
)

prompt = PromptTemplate.from_template(
    """
You are an AI tutor.

Explain {topic} to a {level} student.

Use:
1. Simple definition
2. Example
3. Important points
"""

)

chain = prompt | llm

topic = input("Topic: ")
level = input("Level (beginner/intermediate): ")

result = chain.invoke({
    "topic": topic,
    "level": level
})

print("\nAI TUTOR:")
print(result)