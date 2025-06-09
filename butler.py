from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


raw_document = TextLoader("./information.txt").load()
raw_document_2 = TextLoader("./history.txt").load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
documents = text_splitter.split_documents(raw_document)
documents_2 = text_splitter.split_documents(raw_document_2)

embedd = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text")
db = Chroma.from_documents(documents, embedding=embedd)
db_2 = Chroma.from_documents(documents_2, embedding=embedd)

template = """You are Virtual Butler who helps me in my everyday work. Here is some my information:

{context}

User Command : {question}

Coversation history (Answer only user command and remember things said in conversation history): {history}
"""
prompt = ChatPromptTemplate.from_template(template=template)

model = ChatOllama(
    model= "llama3.2",
)

retriever = db.as_retriever()
retriever_2 = db_2.as_retriever()

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

chain = (
    {"context" : retriever | format_docs, "question" : RunnablePassthrough(), "history" : retriever_2 | format_docs,}
    | prompt
    | model
    | StrOutputParser()
)

response = chain.invoke("Good Evening")

while True:
    print(f"Alpha: {response}")
    query = input("User: ")
    with open("history.txt", "a") as file:
        query_2 = (query+" ")
        file.write(query_2)
    response = chain.invoke(query)