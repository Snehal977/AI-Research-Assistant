import chromadb

client = chromadb.PersistentClient(
    path="vector_db"
)

collection = client.get_collection(
    "admission_docs"
)

question = input(
    "Ask Question: "
)

results = collection.query(
    query_texts=[question],
    n_results=3
)

documents = results["documents"][0]

for i, doc in enumerate(documents):

    print("\n")
    print(f"Result {i+1}")
    print("-" * 50)

    print(doc)