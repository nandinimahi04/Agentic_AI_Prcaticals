from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = add.invoke({
    "a": a,
    "b": b
})

print("Result:", result)