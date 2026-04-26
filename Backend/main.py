from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from nlp import preprocess
from search import search
from llm import generate_response
from memory import save_message, save_response, get_history

# ✅ FIRST create app
app = FastAPI()

# ✅ THEN mount frontend
app.mount("/app", StaticFiles(directory="../frontend", html=True), name="frontend")

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class Query(BaseModel):
    message: str
    user_id: str = "default_user"

# API
@app.post("/chat")
def chat(query: Query):
    user_input = query.message
    user_id = query.user_id

    clean_input = preprocess(user_input)
    history = get_history(user_id)
    raw_answer = search(clean_input)
    final_answer = generate_response(raw_answer, user_input)

    save_message(user_id, user_input)
    save_response(user_id, final_answer)

    return {
        "reply": final_answer,
        "history": history
    }