import chromadb

client = chromadb.PersistentClient(
    path="vector_db"
)

collection = client.get_or_create_collection(
    "admission_docs"
)


def retrieve_chunks(
        question,
        n_results=3):

    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    documents = results["documents"][0]

    return documents
