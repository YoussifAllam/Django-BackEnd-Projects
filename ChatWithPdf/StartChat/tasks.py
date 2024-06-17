from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import FAISS


import os
os.environ["GOOGLE_API_KEY"] = 'AIzaSyCRuE6DsdO6nC9o3MIdCvL5uV411Yo2bHQ'


def Pdf_loader(pdf_path, question):
    from langchain.document_loaders import PyPDFLoader
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain import FAISS

    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(pages, embeddings)
    query = question
    docs = db.similarity_search(query)
    content = "\n".join([x.page_content for x in docs])
    qa_prompt = ("Use the following pieces of context to answer the user's question. "
                 "If you don't know the answer, just say that you don't know, don't try to make up an answer. "
                 "----------------")
    input_text = f"{qa_prompt}\nContext:{content}\nUser question:\n{query}"
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=os.environ["GOOGLE_API_KEY"])
    result = llm.invoke(input_text)
    return result.content