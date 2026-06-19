import chromadb
client = chromadb.PersistentClient(
    path="vector_db"
)

collection = client.get_collection(
    "admission_docs"
)
question="What is admission eligibility?"
results=collection.query(query_texts=[question],n_results=3)
documents=results["documents"][0]
distances = results["distances"][0]
for i,(doc,dist) in enumerate(zip(documents,distances)):
     print("\n")
     print(f"Result {i+1}")
     print("Distance:", dist)
     print("-" * 50)
     print(doc)