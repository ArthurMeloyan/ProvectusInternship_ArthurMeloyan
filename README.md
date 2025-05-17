# Concert Tour Assistant

This project is a Streamlit-based assistant that answers questions about concert tours. It supports two main modes:

1. **RAG mode (Retrieval-Augmented Generation):**  
   Uses your uploaded documents about concert tours to answer questions.

2. **Bonus mode (Online Concert Search):**  
   If no documents are uploaded but you enter a musician or band name, the assistant will search online for upcoming concerts using the SerpAPI.

---

## Setup

### Prerequisites

- Python 3.8+  
- A Hugging Face API token with inference access  
- A SerpAPI API key (for online concert search feature)

### Installation

```bash
pip install -r requirements.txt
