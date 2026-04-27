from sentence_transformers import SentenceTransformer
import numpy as np
import os
import pickle

# Load model safely
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("✅ Model loaded")
except Exception as e:
    print("❌ Model load error:", e)
    model = None

# Path
EMBEDDING_FILE = os.path.join(os.path.dirname(__file__), "../data/embeddings.pkl")

# 🔹 Single embedding
def get_embedding(text):
    try:
        if model is None:
            return None

        if text is None or text.strip() == "":
            return None

        vec = model.encode(text)

        # ensure numpy array
        return np.array(vec)

    except Exception as e:
        print("❌ Embedding error:", e)
        return None


# 🔹 Multiple embeddings
def get_embeddings(text_list):
    try:
        if model is None:
            return None

        if not text_list:
            return None

        vecs = model.encode(text_list)
        return np.array(vecs)

    except Exception as e:
        print("❌ Bulk embedding error:", e)
        return None


# 🔹 Save
def save_embeddings(vectors):
    try:
        with open(EMBEDDING_FILE, "wb") as f:
            pickle.dump(vectors, f)
    except Exception as e:
        print("❌ Save error:", e)


# 🔹 Load
def load_embeddings():
    try:
        if os.path.exists(EMBEDDING_FILE):
            with open(EMBEDDING_FILE, "rb") as f:
                return pickle.load(f)
    except Exception as e:
        print("❌ Load error:", e)

    return None