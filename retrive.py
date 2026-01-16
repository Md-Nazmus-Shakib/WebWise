from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import query_search_vdb
import main
import query
def chat(qry,cont):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2
    )
    prompt = ChatPromptTemplate.from_template("""
    You are a helpful assistant.

    Answer the question using ONLY the context below.
    If the answer is not in the context, say "I searched the document top to bottom, and this answer is playing hide and seek.".

    Context:
    {context}

    Question:
    {question}
    """)
    chain = prompt | llm

    response = chain.invoke({
        "context": cont,
        "question": qry
        
    })
    return response.content