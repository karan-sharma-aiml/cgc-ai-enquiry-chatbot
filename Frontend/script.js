async function sendMessage() {
    let inputField = document.getElementById("userInput");
    let message = inputField.value.trim();

    if (message === "") return;

    let chatbox = document.getElementById("chatbox");
    let typing = document.getElementById("typing");

    // 🟢 Show User Message
    let userDiv = document.createElement("div");
    userDiv.classList.add("message", "user");

    userDiv.innerHTML = `
        <div class="text">${message}</div>
    `;

    chatbox.appendChild(userDiv);

    // Clear input
    inputField.value = "";

    // Auto scroll
    chatbox.scrollTop = chatbox.scrollHeight;

    // 🤖 Show typing
    typing.classList.remove("hidden");

    try {
        // 🔄 Send request to backend (FIXED URL 🔥)
        let response = await fetch("http://127.0.0.1:8001/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message,
                user_id: "user1"
            })
        });

        if (!response.ok) {
            throw new Error("API Error: " + response.status);
        }

        let data = await response.json();

        // ⏳ Fake delay for AI feel
        setTimeout(() => {

            // Hide typing
            typing.classList.add("hidden");

            // 🔵 Show Bot Message
            let botDiv = document.createElement("div");
            botDiv.classList.add("message", "bot");

            botDiv.innerHTML = `
                <div class="text">${data.reply || "No response"}</div>
            `;

            chatbox.appendChild(botDiv);

            chatbox.scrollTop = chatbox.scrollHeight;

        }, 800);

    } catch (error) {
        console.error("Error:", error);

        typing.classList.add("hidden");

        let errorDiv = document.createElement("div");
        errorDiv.classList.add("message", "bot");

        errorDiv.innerHTML = `
            <div class="text">⚠️ Server error. Check backend.</div>
        `;

        chatbox.appendChild(errorDiv);
    }
}

// ⌨️ Enter key support
document.getElementById("userInput").addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});