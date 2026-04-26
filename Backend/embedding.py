from sentence_transformers import SentenceTransformer
import numpy as np
import os
import pickle

# Model load (only once)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Path to save embeddings
EMBEDDING_FILE = os.path.join(os.path.dirname(__file__), "../data/embeddings.pkl")

# Convert single text → vector
def get_embedding(text):
    return model.encode(text)

# Convert multiple texts → vectors
def get_embeddings(text_list):
    return model.encode(text_list)

# Save embeddings to file (for faster loading)
def save_embeddings(vectors):
    with open(EMBEDDING_FILE, "wb") as f:
        pickle.dump(vectors, f)

# Load embeddings if already saved
def load_embeddings():
    if os.path.exists(EMBEDDING_FILE):
        with open(EMBEDDING_FILE, "rb") as f:
            return pickle.load(f)
    return None
