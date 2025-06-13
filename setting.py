import chromadb
from chromadb.config import Settings
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from sentence_transformers import SentenceTransformer
import torch
import os
from transformers import AutoModel
import ChromaRAGSystem

def load_chroma_db(db_path):
    client = chromadb.PersistentClient(path=db_path)
    collections = client.list_collections()
    print(f"Available collections: {[col.name for col in collections]}")
    if not collections:
        raise ValueError("No collections found in the database")
    collection = client.get_collection("korean_catholic_1_1")  # Ensure this matches
    return client, collection

def build_RAG_system(db_path) : 
    client, collection = load_chroma_db(db_path)
    # Set up embedding model (should match what was used to create your vector DB)
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # or your preferred model

    # Set up generation model
    os.environ['TRANSFORMERS_CACHE'] = 'D:/me/Catholic_RAG_system/model'#change your own path
    tokenizer = AutoTokenizer.from_pretrained("Bllossom/llama-3.2-Korean-Bllossom-3B")
    model = AutoModelForCausalLM.from_pretrained("Bllossom/llama-3.2-Korean-Bllossom-3B")

    text_generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=0 if torch.cuda.is_available() else -1
    )

    # Initialize RAG system
    rag_system = ChromaRAGSystem.ChromaRAGSystem(collection, embedding_model, text_generator)
    return rag_system