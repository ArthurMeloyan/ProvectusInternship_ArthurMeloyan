from .retriever import retrieve_similar
from .generator import generate_answer
from online_search import search_concerts

def answer_query(query: str) -> str:
    documents = retrieve_similar(query=query, k=3)
    context = "\n\n".join([doc.page_content for doc in documents])

    prompt = f"""
        You are a helpful assistant. Answer the user's question based on the context below.

        Context:
        {context}

        Question: {query}

        Answer:
    """

    return generate_answer(prompt)
    search_context = search_concerts(query)
    prompt = f"""
    You are a helpful assistant. Use the following web search results to answer the user's question.

    Search Results:
    {search_context}

    Question: {query}

    Answer:
    """
    return generate_answer(prompt)