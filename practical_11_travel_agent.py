from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.5
)

weather = input("Weather: ")
budget = int(input("Budget: "))

if weather.lower() == "rain":
    activity = "indoor activities"

elif budget < 1000:
    activity = "local sightseeing"

else:
    activity = "premium outdoor activities"

prompt = f"""
You are an AI travel agent.

Recommend a simple travel plan.

Activity type: {activity}
Weather: {weather}
Budget: ₹{budget}

Give:
1. Activity
2. Estimated cost
3. Short reason
"""

print(llm.invoke(prompt))