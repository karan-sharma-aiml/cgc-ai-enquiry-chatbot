async function sendMessage() {
    let inputField = document.getElementById("userInput");
    let message = inputField.value.trim();

    if (message === "") return;

    let chatbox = document.getElementById("chatbox");

    // 🟢 Show User Message
    let userDiv = document.createElement("div");
    userDiv.classList.add("message", "user-message");
    userDiv.innerText = message;
    chatbox.appendChild(userDiv);

    // Clear input
    inputField.value = "";

    // Auto scroll
    chatbox.scrollTop = chatbox.scrollHeight;

    try {
        // 🔄 Send request to backend
        let response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: String(message),   // ✅ force string
                user_id: "user1"
            })
        });

        // ❗ check response
        if (!response.ok) {
            throw new Error("API Error: " + response.status);
        }

        let data = await response.json();

        // 🔵 Show Bot Message
        let botDiv = document.createElement("div");
        botDiv.classList.add("message", "bot-message");
        botDiv.innerText = data.reply || "No response";
        chatbox.appendChild(botDiv);

        chatbox.scrollTop = chatbox.scrollHeight;

    } catch (error) {
        console.error("Error:", error);

        let errorDiv = document.createElement("div");
        errorDiv.classList.add("message", "bot-message");
        errorDiv.innerText = "⚠️ Error: " + error.message;
        chatbox.appendChild(errorDiv);
    }
}
document.getElementById("userInput").addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});