from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
# Load your documents
loader = TextLoader("./data/documents.txt")  # Adjust to your data file
documents = loader.load()

# Split large documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                               chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Generate embeddings and store in FAISS
embeddings = OpenAIEmbeddings(openai_api_key='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')
vectorstore = FAISS.from_documents(docs, embeddings)

# Save the vectorstore
vectorstore.save_local("faiss_index")
print("Vectorstore created and saved locally.")
