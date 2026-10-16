from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.4
)

topic = input("Research topic: ")

research = llm.invoke(
    f"""
You are a Research Agent.

Research important points about:

{topic}
"""
)

summary = llm.invoke(
    f"""
You are a Report Writer Agent.

Convert these research notes into
a short structured report:

{research}
"""
)

print("\nRESEARCH AGENT:")
print(research)

print("\nWRITER AGENT:")
print(summary)