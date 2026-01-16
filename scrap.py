import requests
from bs4 import BeautifulSoup
import main
import clean
import chunk
import embeding
import chromadb
def doc_scrap(url_n):
    url = url_n

    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")
    text = soup.get_text(separator="\n")

    with open("api_docs.txt","w",encoding="utf-8") as f:
        f.write(text)
    print("Saved!")
# print(soup.text.strip())
# headings = soup.find("")

# for h in headings:
#     print(h.text.strip())


#clean the text

    with open ("api_docs.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    cleaned_text = clean.clean_text(raw_text)

    with open("cleaned_docs.txt","w",encoding="utf-8") as f:
        f.write(cleaned_text)
    return cleaned_text
    
    chunks = chunk.chunk_text(cleaned_text)

# Embedding
    embeded_output = embeding.emnbedding(chunks)
    try:
        dims = embeded_output.shape[1]
    except Exception:
    # Fallback if embeddings is a list of lists
        dims = len(embeded_output[0]) if embeded_output and embeded_output[0] is not None else 0
# print(f"Each embedding has {dims} dimensions")
# print(embeded_output)
    return chunks,embeded_output,url

