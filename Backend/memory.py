# Simple in-memory storage (dictionary)
chat_memory = {}

# Save user message
def save_message(user_id, message):
    if user_id not in chat_memory:
        chat_memory[user_id] = []

    chat_memory[user_id].append({"role": "user", "message": message})


# Save bot response
def save_response(user_id, response):
    if user_id not in chat_memory:
        chat_memory[user_id] = []

    chat_memory[user_id].append({"role": "bot", "message": response})


# Get full chat history
def get_history(user_id):
    return chat_memory.get(user_id, [])


# Clear memory (optional)
def clear_history(user_id):
    if user_id in chat_memory:
        chat_memory[user_id] = []