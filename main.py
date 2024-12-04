from flask import Flask, render_template, request
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

# Initialize Flask app
app = Flask(__name__)

# Load FAISS vector store
embeddings = OpenAIEmbeddings(openai_api_key='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')
vectorstore = FAISS.load_local("faiss_index", embeddings=embeddings, allow_dangerous_deserialization=True)

# Set up retriever
retriever = vectorstore.as_retriever()

# Initialize ChatOpenAI and ConversationalRetrievalChain
llm = ChatOpenAI(temperature=0.3, openai_api_key='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')
qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever)

# Initialize chat history
chat_history = []  # Store chat history for conversational flow

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    global chat_history  # Use global chat history for simplicity
    if request.method == 'POST':
        prompt = request.get_json().get('prompt')

        # Run the QA chain with the user input and chat history
        output = qa_chain.invoke({
            "question": prompt,
            "chat_history": chat_history,
        })

        # Update chat history with the latest interaction
        chat_history.append((prompt, output["answer"]))

        return output["answer"]
    else:
        return "Invalid Request"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)