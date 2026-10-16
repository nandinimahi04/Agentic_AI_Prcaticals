from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0
)

task = input("Enter task: ")

expert = llm.invoke(
    f"""
Choose the best specialist for this task.

Options:
MATH
PYTHON
WRITING

Task:
{task}

Return ONLY the specialist name.
"""
).strip()

print("Supervisor selected:", expert)

answer = llm.invoke(
    f"""
You are a {expert} expert.

Solve the following task:

{task}
"""
)

print("\nAnswer:")
print(answer)