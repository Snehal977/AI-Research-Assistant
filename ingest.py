import chromadb
from utils.pdf_loader import load_pdf
from utils.chunking import clean_text
from utils.chunking import create_chunk
from dashboards.analytics import document_statistics
pdf_name = input(
    "Enter PDF name: "
)

pdf_path = f"data/{pdf_name}"
text=load_pdf(pdf_path)
print("PDF loaded")
text=clean_text(text)
print("text cleaned")
chunks=create_chunk(text,chunk_size=1000,overlap=200)
print("total chunks:",len(chunks))
client=chromadb.PersistentClient(path="vector_db")
collection=client.get_or_create_collection(name="admission_docs")
ids=[]
for i in range(len(chunks)):
    ids.append(f"chunk_{i}")
metadatas=[]
for i in range(len(chunks)):
    metadatas.append({"source":"admission_chatbot_OG","chunk_id":i})
if collection.count() > 0:
    collection.delete(
        ids=collection.get()["ids"]
    )    
collection.add(documents=chunks,ids=ids,metadatas=metadatas)    
print("database stored chunks count:",collection.count())    