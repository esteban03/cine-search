# 🔍 Semantic Search with Sentence Transformers

A simple example demonstrating semantic search using open-source embeddings and the `sentence-transformers` library. This project searches through a collection of Tarantino movies using natural language queries.

## 🤔 What is Semantic Search?

Semantic search understands the meaning behind your query rather than just matching keywords. Instead of searching for exact word matches, it finds content that is conceptually similar to your query using vector embeddings.

## ⚙️ How it Works

1. **Text Encoding**: The `sentence-transformers` library converts movie descriptions into high-dimensional vectors (embeddings) that capture semantic meaning
2. **Query Processing**: Your search query is converted into the same vector space  
3. **Similarity Matching**: The system finds movies with embeddings most similar to your query using cosine similarity
4. **Results**: Returns the best matching movie based on semantic similarity scores

## ✨ Features

- Uses the `all-MiniLM-L6-v2` model for fast, accurate embeddings
- Searches through Tarantino movie database with English descriptions
- Demonstrates vector similarity scoring
- Lightweight and easy to understand implementation

## 📋 Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

## 🚀 Installation

### Install uv (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Run the Project

```bash
# Clone or navigate to the project directory
cd search

# Install dependencies and run
uv run main.py
```

That's it! `uv` automatically:
- Creates a virtual environment
- Installs all dependencies from `pyproject.toml`
- Runs the script

## 💻 Usage

### Basic Example

The current example searches for "fading actor in decline" and finds the most semantically similar Tarantino movie:

```python
query = "fading actor in decline"
# Results in finding "Once Upon a Time in Hollywood" 
# which features an actor facing career decline
```

### Try Different Queries

Edit `main.py` and modify the query:

```python
query = "violent revenge story"  # Will likely match Kill Bill
query = "war movie"              # Will likely match Inglourious Basterds  
query = "western"                # Will likely match Django Unchained
```

## 🎨 Customization

### Add Your Own Data

Replace the movie data in `data.py` with your own content:

```python
your_data = [
    {
        "title": "Your Title",
        "description": "Your description here...",
        # Add any other fields you want to search
    }
]
```

Then update the text formatting in `main.py` to match your data structure.

## 📦 Dependencies

- **sentence-transformers**: Provides pre-trained models for text embeddings
- **numpy**: Numerical operations for vector similarity calculations

## ⚡ Performance Notes

This implementation runs on CPU using `.cpu().numpy()` to ensure compatibility across all systems. While GPU acceleration with NVIDIA CUDA would be faster for larger datasets, CPU processing is:

- **Universal**: Works on Mac (Apple Silicon/Intel) and Linux
- **Educational**: Easier setup for learning - no GPU drivers required  
- **Sufficient**: Fast enough for small to medium datasets like this movie collection

For production applications with larger datasets, consider GPU acceleration if available.

## 🎯 Why This Example?

This project demonstrates key concepts in modern AI applications:

- **Vector Embeddings**: How text becomes numerical representations
- **Semantic Understanding**: Moving beyond keyword matching
- **Similarity Search**: Finding related content in high-dimensional space
- **Open Source AI**: Using freely available, high-quality models

Perfect for learning the foundations of semantic search before scaling to larger datasets or more complex applications.

## 🚀 Next Steps

- Experiment with different sentence transformer models
- Add more sophisticated ranking algorithms
- Implement vector databases for larger datasets (Pinecone, Weaviate, ChromaDB)
- Build a web interface with FastAPI or Flask