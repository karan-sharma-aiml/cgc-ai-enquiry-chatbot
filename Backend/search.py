import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from embedding import get_embedding, get_embeddings, load_embeddings, save_embeddings

# Load FAQ data
with open("../data/faq.json", "r", encoding="utf-8") as f:
    faq = json.load(f)

# Extract questions
questions = [item["question"] for item in faq]

# Load embeddings
question_vectors = load_embeddings()

if question_vectors is None:
    print("⚡ Creating embeddings (first time)...")
    question_vectors = get_embeddings(questions)
    save_embeddings(question_vectors)
else:
    print("✅ Loaded saved embeddings")

# 🔍 Search function
def search(query, threshold=0.5):
    try:
        # 🧠 Convert query to vector
        query_vec = get_embedding(query)

        # ❌ FIX 1: Check embedding
        if query_vec is None:
            return "Sorry, system error (embedding failed)"

        # ❌ FIX 2: Check stored embeddings
        if question_vectors is None or len(question_vectors) == 0:
            return "Knowledge base not loaded properly"

        # 🔍 Similarity
        scores = cosine_similarity([query_vec], question_vectors)[0]

        # Best match
        best_index = int(np.argmax(scores))
        best_score = float(scores[best_index])

        print(f"Best score: {best_score}")

        # ❌ FIX 3: Threshold fallback
        if best_score < threshold:
            return "Sorry, mujhe samajh nahi aaya. Please thoda clear poochiye 🙏"

        # ✅ Return answer safely
        return faq[best_index].get("answer", "No answer found")

    except Exception as e:
        print("❌ SEARCH ERROR:", str(e))
        return "Internal error in search system"