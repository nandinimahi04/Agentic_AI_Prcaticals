from transformers import pipeline

classifier = pipeline(
    "image-classification"
)

image = input("Enter image path: ")

results = classifier(image)

label = results[0]["label"]
score = results[0]["score"]

print("\nPerception:", label)
print(
    "Confidence:",
    round(score, 2)
)

if score > 0.7:

    print("Agent Action: Accept prediction")

else:

    print("Agent Action: Request human review")