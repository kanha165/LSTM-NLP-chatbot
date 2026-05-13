async function sendMessage() {

    const input = document.getElementById("user-input");

    const message = input.value;

    if (message.trim() === "") return;

    const chatBox = document.getElementById("chat-box");

    // USER MESSAGE

    chatBox.innerHTML += `
        <div class="message user">
            ${message}
        </div>
    `;

    input.value = "";

    // API CALL

    const response = await fetch(
        `http://127.0.0.1:8000/chat?message=${message}`
    );

    const data = await response.json();

    // BOT MESSAGE

    chatBox.innerHTML += `
        <div class="message bot">
            ${data.response}
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}