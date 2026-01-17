# 🔍 WebWise

WebWise is a powerful RAG (Retrieval-Augmented Generation) application that allows you to ask questions about any webpage content. It scrapes web pages, processes the content, and uses AI to provide accurate answers based solely on the scraped information.

## ✨ Features

- **Web Scraping**: Extract content from any publicly accessible webpage
- **Intelligent Text Processing**: Automatically cleans and chunks text for optimal processing
- **Vector Database Storage**: Uses ChromaDB for efficient semantic search
- **AI-Powered Q&A**: Leverages Groq's Llama 3.3 70B model for accurate answers
- **Semantic Search**: Finds relevant context using sentence transformers embeddings
- **Interactive Web Interface**: Beautiful Streamlit UI for easy interaction
- **Session Management**: Maintains conversation context within the same session

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Groq API key (get it from [Groq Console](https://console.groq.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Md-Nazmus-Shakib/WebWise.git
   cd WebWise
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

### Usage

1. **Run the Streamlit application**
   ```bash
   streamlit run main.py
   ```

2. **Process a webpage**
   - Enter the webpage URL in the sidebar
   - Provide a collection name (for storing embeddings)
   - Click "Process Document"

3. **Ask questions**
   - Once processing is complete, type your question in the input box
   - Get AI-powered answers based on the webpage content

## 📁 Project Structure

```
WebWise/
├── main.py                 # Streamlit web application (entry point)
├── scrap.py               # Web scraping functionality
├── clean.py               # Text cleaning and preprocessing
├── chunk.py               # Text chunking for processing
├── embeding.py            # Text embedding generation (note: filename has typo)
├── vector_db.py           # ChromaDB vector database operations
├── query.py               # Query embedding generation
├── query_search_vdb.py    # Semantic search in vector database
├── retrive.py             # LLM integration for answer generation (note: filename has typo)
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (create this)
└── chroma_db/            # ChromaDB storage directory (auto-created)
```

## 🛠️ Technology Stack

- **Web Framework**: Streamlit
- **Web Scraping**: BeautifulSoup4, Requests
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Vector Database**: ChromaDB
- **LLM Framework**: LangChain
- **AI Model**: Groq (Llama 3.3 70B Versatile)
- **Additional Libraries**: OpenAI, Pandas

## 🔧 How It Works

1. **Scraping**: The application downloads and parses the HTML content from the provided URL
2. **Cleaning**: Removes unnecessary content and keeps relevant text
3. **Chunking**: Splits the text into manageable chunks (200 words each)
4. **Embedding**: Converts text chunks into vector embeddings using sentence transformers
5. **Storage**: Stores embeddings in ChromaDB for efficient retrieval
6. **Query Processing**: When you ask a question, it's converted to an embedding
7. **Semantic Search**: Finds the most relevant chunks from the vector database
8. **Answer Generation**: Uses Groq's Llama model to generate answers based on the retrieved context

## 📝 Example Use Cases

- Research and analyze documentation websites
- Extract information from blog posts and articles
- Query product documentation
- Analyze news articles and reports
- Study educational content from web pages

## ⚙️ Configuration

### Chunking
Modify chunk size in `chunk.py`:
```python
def chunk_text(text, chunk_size=200):  # Adjust chunk_size as needed
```

### Embedding Model
Change the model in `embeding.py` (filename has a typo):
```python
model = SentenceTransformer('all-MiniLM-L6-v2')  # Try other models
```

### LLM Model
Update the model in `retrive.py` (filename has a typo):
```python
model="llama-3.3-70b-versatile"  # Use other Groq models
```

### Search Results
Adjust number of results in `query_search_vdb.py`:
```python
n_results=4  # Change to retrieve more/fewer chunks
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Md Nazmus Shakib**
- GitHub: [@Md-Nazmus-Shakib](https://github.com/Md-Nazmus-Shakib)

## 🙏 Acknowledgments

- Groq for providing fast LLM inference
- ChromaDB for vector database capabilities
- Sentence Transformers for embedding models
- Streamlit for the amazing web framework

---

**Note**: Make sure to keep your API keys secure and never commit them to version control!
