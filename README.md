# AI Article Generator

This project is a web application designed to generate high-quality articles based on user-provided prompts. It leverages LangChain, OpenAI, and FAISS to create an efficient Retrieval-Augmented Generation (RAG) pipeline. This ensures that the AI generates content grounded in a custom dataset provided by the user.

---

## Features

- **Custom Data Learning**: Uses a `documents.txt` file to provide the AI with domain-specific knowledge.
- **RAG Implementation**: Ensures accurate and contextually relevant articles by combining document retrieval with OpenAI’s powerful LLMs.
- **User-Friendly Interface**: Provides an easy-to-use web interface built with Flask.
- **Efficient Storage and Retrieval**: Utilizes FAISS for fast and scalable vector-based information retrieval.
- **Customizable Workflow**: Allows users to fine-tune the AI’s behavior, data, and underlying components.

---

## Project Setup

### Prerequisites

- Python 3.10
- `pip` (Python package installer)
- OpenAI API key ([Get it here](https://platform.openai.com/account/api-keys))
- LangChain

---

### Installation Steps

#### 1. Clone the Repository

Clone this project to your local machine:

```bash
git clone https://github.com/your-repository-link.git
cd AI-Article-Generator
```

#### 2. Install Dependencies

Run the following command to install all required Python packages:

```bash
pip install -r requirements.txt
```

#### 3. Prepare Your Data

Create a `documents.txt` file inside a `data` directory in your project root:

```
mkdir data
nano data/documents.txt
```

Populate this file with the content you want the AI to learn from. This could be blog posts, articles, or any other text data.

---

### Building the FAISS Index

To enable RAG, create a FAISS index from your `documents.txt` file by running:

```bash
python prepare_data.py
```

This will generate a FAISS index named `faiss_index` in your project directory. The FAISS index is used to store and retrieve vectorized representations of your data.

---

### Configure Your OpenAI API Key

1. Create a `.env` file in the project root:
   ```bash
   touch .env
   nano .env
   ```
2. Add your OpenAI API key to the `.env` file:
   ```plaintext
   OPENAI_API_KEY=YOUR_OPENAI_API_KEY
   ```
3. Ensure the `python-dotenv` package is installed:
   ```bash
   pip install python-dotenv
   ```

---

### Running the Application

Start the Flask server by running:

```bash
python main.py
```

This will launch the server on `http://0.0.0.0:81`.

---

### Using the Web Application

1. Open your browser and navigate to `http://0.0.0.0:81`.
2. Enter the desired title or topic for your article in the provided textarea.
3. Click the "Submit" button.
4. The generated article will appear in the "Your content will show up here" section.
5. If the topic is not found in your dataset, an error will be displayed.

---

## How It Works

This application implements **Retrieval-Augmented Generation (RAG)** to generate accurate, relevant articles:

1. **Data Ingestion and Indexing**:

   - The `prepare_data.py` script processes the `documents.txt` file and vectorizes its contents using OpenAI embeddings.
   - These embeddings are stored in a FAISS index for efficient retrieval.

2. **Prompt Handling**:

   - When a user submits a prompt (title), the application queries the FAISS index to retrieve the most relevant chunks of text.

3. **Generation with OpenAI**:

   - The retrieved data is used as context to guide the OpenAI LLM in generating the article.
   - This ensures the output is both accurate and grounded in the provided dataset.

4. **Web Interface**:

   - The Flask-based interface simplifies interaction with the AI, allowing users to generate articles seamlessly.

---

## RAG Implementation Details

The project integrates **Retrieval-Augmented Generation (RAG)** using the following components:

### 1. **FAISS Vector Store**:

- **Purpose**: Efficiently stores and retrieves vectorized text data.
- **Creation**: The `prepare_data.py` script converts the `documents.txt` content into embeddings and stores them in FAISS.
- **Usage**: During runtime, the FAISS index retrieves the most relevant text chunks based on the user’s query.

### 2. **LangChain Framework**:

- **Purpose**: Orchestrates the interaction between the FAISS index, OpenAI LLM, and user inputs.
- **Retrieval Chain**: Combines the FAISS retriever with OpenAI’s text generation capabilities.

### 3. **OpenAI LLM**:

- **Purpose**: Generates the article based on the retrieved context and user prompt.
- **Customization**: Supports fine-tuning the prompt to improve the quality of the generated content.

---

## Customization Options

### 1. **Data**:

Modify the `documents.txt` file to train the AI on your desired dataset.

### 2. **LLM**:

Change the OpenAI model (e.g., `text-davinci-003`, `gpt-4`) by adjusting the `llm` configuration in `main.py`.

### 3. **Vector Store**:

Replace FAISS with other vector stores like Chroma or Pinecone by updating the relevant code in `prepare_data.py` and `main.py`.

### 4. **Prompt Engineering**:

Enhance the prompts in `main.py` to guide the AI toward better article generation.

---

## Potential Improvements

### Advanced Features:

- **Sophisticated Prompts**: Implement advanced prompt engineering techniques.
- **Fine-Tuning**: Train the LLM with specific datasets for improved accuracy.

### UI Enhancements:

- Add features for editing, saving, and sharing generated articles.
- Include a progress bar for longer article generation tasks.

### Content Moderation:

- Integrate tools to filter and moderate generated content, ensuring ethical and compliant outputs.

---

## Conclusion

This project provides a robust foundation for building an AI-powered article generator. By leveraging RAG, LangChain, and OpenAI, it ensures that the generated content is both relevant and high-quality. With additional customization and improvements, it can be adapted to various use cases, from blogging to enterprise content generation.

