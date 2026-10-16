from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.4
)

subject = input("Subject: ")
hours = int(input("Available hours: "))

prompt = f"""
You are a study planning agent.

Subject: {subject}
Available hours: {hours}

Break the study goal into smaller tasks.

Requirements:
- Prioritize difficult topics first.
- Assign approximate time.
- Include short revision.
- Provide a final schedule.
"""

result = llm.invoke(prompt)

print("\nSTUDY PLAN:")
print(result)