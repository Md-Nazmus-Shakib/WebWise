# from dotenv import load_dotenv
# import os 
# import scrap
# import vector_db
# import query_search_vdb
# import query
# import retrive
# import chunk
# import embeding
# load_dotenv()
# api_key = os.getenv("GROQ_API_KEY")
# # print("Groq API Key loaded:", api_key is not None)

# def main():
    
#     ur = input("Enter your link: ")
#     cl_name = input("Enter ypur collection name: ")
#     scraped_clean_text = scrap.doc_scrap(ur)
#     chunks = chunk.chunk_text(scraped_clean_text)
#     embeded_output = embeding.emnbedding(chunks)
#     col = vector_db.vector_store(cl_name,chunks,embeded_output,ur)
    
#     qn = input("Enter your query: ")
#     while qn!="ok":
#         query_output = query.query_embeding(qn)
#         con = query_search_vdb.semantic_search(query_output,col)
#         # print(con)
#         final_response = retrive.chat(qn, con)
#         print(final_response)
#         qn = input("Enter your query: ")

# if __name__ == "__main__":
#     main()


import streamlit as st
from dotenv import load_dotenv
import os

import scrap
import chunk
import embeding
import vector_db
import query
import query_search_vdb
import retrive

# Load env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Web RAG Agent", layout="wide")

st.title("🔍 Web Document Q&A Agent")
st.write("Ask questions based **only** on a scraped webpage")

# -----------------------------
# Session State Initialization
# -----------------------------
if "collection" not in st.session_state:
    st.session_state.collection = None

if "ready" not in st.session_state:
    st.session_state.ready = False

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("Setup")

url = st.sidebar.text_input("Enter webpage URL")
collection_name = st.sidebar.text_input("Collection name")

if st.sidebar.button("Process Document"):
    with st.spinner("Scraping and processing document..."):
        text = scrap.doc_scrap(url)
        chunks = chunk.chunk_text(text)
        embeddings = embeding.emnbedding(chunks)

        col = vector_db.vector_store(
            collection_name,
            chunks,
            embeddings,
            url
        )

        st.session_state.collection = col
        st.session_state.ready = True

    st.sidebar.success("Document processed successfully!")

# -----------------------------
# Question Answering
# -----------------------------
st.header("Ask a Question")

if not st.session_state.ready:
    st.info("👈 Please process a document first")
else:
    user_query = st.text_input("Your question")

    if user_query:
        with st.spinner("Searching..."):
            q_embedding = query.query_embeding(user_query)
            context = query_search_vdb.semantic_search(
                q_embedding,
                st.session_state.collection
            )

            answer = retrive.chat(user_query, context)

        st.subheader("Answer")
        st.write(answer)
