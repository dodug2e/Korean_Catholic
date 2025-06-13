class ChromaRAGSystem:
    def __init__(self, collection, embedding_model, generator):
        self.collection = collection
        self.embedding_model = embedding_model
        self.generator = generator
    
    def retrieve_relevant_docs(self, query, n_results=5):
        """Retrieve relevant documents from Chroma DB"""
        # Create query embedding
        query_embedding = self.embedding_model.encode([query]).tolist()
        
        # Search in Chroma DB
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        
        return results
    
    def generate_response(self, query, context_docs):
        """Generate response using retrieved context"""
        # Combine retrieved documents into context
        context = "\n".join([doc for doc in context_docs['documents'][0]])
        
        # Create prompt with context
        prompt = f"""Context: {context}
        
Question: {query}

Answer based on the context provided:"""
        
        # Generate response
        response = self.generator(
            prompt,
            max_length=len(prompt.split()) + 100,
            num_return_sequences=1,
            pad_token_id=self.generator.model.config.eos_token_id  # or simply omit this argument
        )
        
        return response[0]['generated_text'][len(prompt):].strip()
    
    def query(self, question):
        """Main RAG pipeline"""
        # Step 1: Retrieve relevant documents
        relevant_docs = self.retrieve_relevant_docs(question)
        
        # Step 2: Generate response using context
        response = self.generate_response(question, relevant_docs)
        
        return {
            'answer': response,
            'sources': relevant_docs['documents'][0],
            'metadata': relevant_docs.get('metadatas', [None])[0]
        }