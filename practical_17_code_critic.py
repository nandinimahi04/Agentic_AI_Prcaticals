from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.3
)

task = input("Programming requirement: ")

code = llm.invoke(
    f"""
Write Python code for:

{task}

Return only the code.
"""
)

review = llm.invoke(
    f"""
Act as a code reviewer.

Review the following Python code:

{code}

Identify:
1. Errors
2. Bugs
3. Improvements
"""
)

print("\nGENERATED CODE:")
print(code)

print("\nCRITIC:")
print(review)