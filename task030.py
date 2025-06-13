import chromadb
from chromadb.config import Settings
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from sentence_transformers import SentenceTransformer
import torch
import os
from transformers import AutoModel
import ChromaRAGSystem
import setting


rag_system = setting.build_RAG_system("./korean_catholic_data")

while True : 
    question = input("질문을 입력하세요 : ")

    if question == "quit" or question == "종료" : 
        break
    
    result = rag_system.query(question)

    print("Question:", question)
    print("Answer:", result['answer'])
    print("\nSources used:")
    for i, source in enumerate(result['sources']):  # Show top 3 sources
        print(f"{i+1}. {source[:200]}...")