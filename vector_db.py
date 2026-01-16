import scrap
import main
import chromadb
def vector_store(cname,chunks,embeded_output,url):
    CHROMA_PATH = r"chroma_db"
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = chroma_client.get_or_create_collection(name=cname)

    documents = []
    metadata = []
    ids = []
    embeddings = []

    # Pair each chunk with its embedding and construct Chroma inputs
    for i, (doc, emb) in enumerate(zip(chunks,embeded_output)):
        documents.append(doc)
        ids.append(f"ID{i}")
        metadata.append({
            "source": url,
            "chunk_index": i,
            "length": len(doc)
        })
        # Ensure embeddings are plain Python lists
        try:
            embeddings.append(emb.tolist())
        except AttributeError:
            embeddings.append(list(emb))
    
        collection.upsert(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadata,
        ids=ids)
        return collection

     
 
