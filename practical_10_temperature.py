from langchain_ollama import OllamaLLM

low = OllamaLLM(
    model="llama3.2",
    temperature=0.1
)

high = OllamaLLM(
    model="llama3.2",
    temperature=1.0
)

prompt = "Write a creative sentence about Artificial Intelligence."

print("LOW TEMPERATURE:")
print(low.invoke(prompt))

print("\nHIGH TEMPERATURE:")
print(high.invoke(prompt))


#
#| Temperature | Behavior           |
#| ----------- | ------------------ |
#| `0.0–0.2`   | More deterministic |
#| `0.3–0.6`   | Balanced           |
#| `0.7–1.0`   | More creative      |

