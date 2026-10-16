from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.3
)

prompt = PromptTemplate.from_template(
    """
Explain {topic} in simple words for a student.

Give:
- Definition
- Example
- Advantages
"""

)

chain = prompt | llm

topic = input("Enter topic: ")

print(chain.invoke({
    "topic": topic
}))