#RAG (Retrieval-Augmented Generation):
#“It is a technique where the system first retrieves relevant data and then generates a response based on that information.”
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from nlp import preprocess
from search import search
from llm import generate_response
from memory import save_message, save_response, get_history

# ✅ Create app
app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request model
class Query(BaseModel):
    message: str
    user_id: str = "default_user"

# ✅ SINGLE API ROUTE (ONLY ONE 🔥)
@app.post("/chat")
def chat(query: Query):
    try:
        print("📥 Received:", query.message)

        user_input = query.message
        user_id = query.user_id

        clean_input = preprocess(user_input)
        print("🧹 Clean:", clean_input)

        history = get_history(user_id)

        raw_answer = search(clean_input)
        print("🔍 Answer:", raw_answer)

        final_answer = generate_response(raw_answer, user_input)

        save_message(user_id, user_input)
        save_response(user_id, final_answer)

        return {
            "reply": final_answer,
            "history": history
        }

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"reply": "Backend error occurred"}

# ✅ Mount frontend LAST
app.mount("/app", StaticFiles(directory="../frontend", html=True), name="frontend")