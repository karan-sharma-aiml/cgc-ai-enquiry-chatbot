import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from embedding import get_embedding, get_embeddings, load_embeddings, save_embeddings

# Load FAQ data
with open("../data/faq.json", "r", encoding="utf-8") as f:
    faq = json.load(f)

# Extract questions
questions = [item["question"] for item in faq]

# Load saved embeddings OR create new ones
question_vectors = load_embeddings()

if question_vectors is None:
    print("⚡ Creating embeddings (first time)...")
    question_vectors = get_embeddings(questions)
    save_embeddings(question_vectors)
else:
    print("✅ Loaded saved embeddings")

# 🔍 Search function
def search(query, threshold=0.5):
    # Convert user query to vector
    query_vec = get_embedding(query)

    # Calculate similarity
    scores = cosine_similarity([query_vec], question_vectors)[0]

    # Get best match
    best_index = np.argmax(scores)
    best_score = scores[best_index]

    # Debug print (optional)
    print(f"Best score: {best_score}")

    # If similarity is too low → fallback
    if best_score < threshold:
        return "Sorry, mujhe samajh nahi aaya. Please thoda clear poochiye 🙏"

    # Return best answer
    return faq[best_index]["answer"]