from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

data = [
    "College starts at 9 AM.",
    "Library is open from 8 AM to 8 PM.",
    "Exam cell is located in Block A.",
    "Students must carry their ID cards."
]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_texts(
    data,
    embeddings
)

question = input("Ask college question: ")

docs = db.similarity_search(
    question,
    k=1
)

print("\nRetrieved Information:")
print(docs[0].page_content)