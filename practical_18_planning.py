from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.4
)

task = input("Enter task: ")

plan = llm.invoke(
    f"""
Create exactly 3 steps to complete:

{task}
"""
)

execution = llm.invoke(
    f"""
Execute this plan conceptually.

Plan:
{plan}

Give the expected outcome.
"""
)

print("\nPLAN:")
print(plan)

print("\nEXECUTION:")
print(execution)