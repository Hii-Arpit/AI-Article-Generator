# AI Article Generator
This project provides a simple web application that generates Articles based on user-provided prompts using a combination of LangChain and OpenAI.

# Project Setup

## Prerequisites:
* Python 3.10
* pip
* OpenAI API key (you can obtain one from https://platform.openai.com/account/api-keys)
* Langchain


## Install dependencies:

`pip install -r requirements.txt`

## Prepare your data:

* Create a text file named documents.txt in a data directory.
* Populate this file with the content you want your AI to learn from. This could be existing blog posts, articles, or any other relevant text.
### Create a FAISS index:
**Run the following command in your terminal:**
`python prepare_data.py`

This will generate a FAISS index file named faiss_index in your project directory.

## Set your OpenAI API key:

* Create a .env file in your project root directory.
* Add the following line to the .env file, replacing YOUR_OPENAI_API_KEY with your actual API key:
 
     `OPENAI_API_KEY=YOUR_OPENAI_API_KEY`

Make sure you have the python-dotenv package installed: 

`pip install python-dotenv`

## Running the Application
* Start the Flask server:

  `python main.py`

This will start the server on http://0.0.0.0:81.

## Access the web application:
Open your browser and navigate to http://0.0.0.0:81.

## Generate a Article:

* Enter your desired title in the provided textarea according to the data you provided in the documents.txt
* Click the "Submit" button.
* The generated Article will appear in the "Your content will show up here" section.
* If the Article topic is not found in the data you provided it will throw error

## How it Works
* The application utilizes a combination of LangChain and OpenAI to generate Articles.
* LangChain is a powerful framework that helps to structure and connect different components of AI applications.
* OpenAI provides the LLM (large language model) that is used to generate the text.
* The project uses a FAISS vector store to efficiently store and retrieve relevant information from the text data.
* The web application allows users to provide a prompt (in this case, the title) and receive a generated Article.

## Customization
* Data: You can customize the data used to train the AI by modifying the documents.txt file.
* LLM: You can choose a different OpenAI LLM or a different LLM provider by adjusting the llm configuration in main.py.
* Vector store: You can experiment with different vector stores (e.g., Chroma, Pinecone) by changing the relevant code in prepare_data.py and main.py.
* RetrievalQA Chain: You can modify the RetrievalQA chain in main.py to customize the way the AI processes prompts and retrieves information.
## Potential Improvements
* More sophisticated prompt handling: Implement more advanced prompt engineering techniques to guide the AI in generating better Articles.
* Fine-tuning: Fine-tune the LLM with a specific dataset to improve its performance on generating Articles.
* User interface: Design a more user-friendly interface with features like editing, saving, and sharing generated content.
* Content filtering and moderation: Integrate content filtering mechanisms to ensure generated content meets ethical standards.

This project provides a solid foundation for building a functional AI Article generator.
