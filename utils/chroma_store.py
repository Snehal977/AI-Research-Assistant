import chromadb

client = chromadb.PersistentClient(
    path="vector_db"
)

collection = client.get_or_create_collection(
    name="admission_docs"
)


def store_chunks(chunks):

    # Clear old chunks

    if collection.count() > 0:

        old_ids = collection.get()["ids"]

        collection.delete(
            ids=old_ids
        )

    ids = []

    for i in range(len(chunks)):

        ids.append(
            f"chunk_{i}"
        )

    collection.add(
        documents=chunks,
        ids=ids
    )

    return collection.count()