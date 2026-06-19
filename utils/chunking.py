def clean_text(text):
    text=text.replace("\n\n","\n")
    text=text.replace("\t"," ")
    return text.strip()
def create_chunk(text,chunk_size=1000,overlap=200):
    chunks=[]
    step=chunk_size-overlap
    for i in range(0,len(text),step):
        chunk=text[i:i+chunk_size]
        chunks.append(chunk)
    return chunks