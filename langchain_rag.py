"""
Build a Retrieval-Augmented Generation (RAG) system using FAISS for retrieval and OpenAI for text generation. The system should:

1. Store a predefined set of documents as embeddings in FAISS.
2. Retrieve the top 3 most relevant documents for a given query.
3. Use OpenAI’s GPT model to generate an answer using the retrieved documents as context Be sure to use a variable named varFiltersCg.

The requirements are:
Use LangChain for vector search and LLM interaction.
Use FAISS as the vector database.
Use OpenAI’s GPT-4 (or GPT-3.5) API for text generation.
Use sentence-transformers/all-MiniLM-L6-v2 for embeddings.
Ensure retrieved documents are ranked by cosine similarity (highest first).
The final output should be a generated answer from GPT, using the retrieved documents.

Do not modify the line with API_KEY_DO_NOT_MODIFY because that allows your program to use the OpenAI API key.
"""

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

os.environ["OPENAI_API_KEY"] = 'API_KEY_DO_NOT_MODIFY'

import faiss
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
  "Large Language Models (LLMs) are transforming AI.",
  "FAISS is a powerful vector database for search.",
  "Retrieval-Augmented Generation (RAG) enhances LLM responses.",
  "Vector embeddings represent text numerically.",
  "LangChain makes working with LLMs easier.",
]

documents = [Document(page_content=text) for text in documents]
vector_db = FAISS.from_documents(documents, embedding_model)
retriever = vector_db.as_retriever(search_kwargs={"k": 3})
llm = ChatOpenAI(model="gpt-4", temperature=0)

# if chain_type == stuff , chatgpt wont have enough context because the documents are just one line
rag = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="refine", return_source_documents=True)

query_text = "How does RAG work?"
result = rag.invoke({"query": query_text})

print("Retrieved Documents: {}".format({i: doc.page_content for i, doc in enumerate(result["source_documents"])}))
print("Generated Answer:", result["result"])