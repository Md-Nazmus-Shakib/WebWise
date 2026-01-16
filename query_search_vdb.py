import query
import vector_db
import langchain
def semantic_search(qo,coll):
    results = coll.query(
        query_embeddings = [qo],
        n_results=4
    )
    documents = results["documents"][0]
    context = "\n\n".join(documents)
    return context
# print(context)