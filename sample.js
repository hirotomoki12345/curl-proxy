<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ChatGPT Demo</title>
</head>
<body>
  <h1>Chat with ChatGPT</h1>
  <div>
    <label for="message">Your Message:</label>
    <input type="text" id="message" />
    <button id="sendMessage">Send</button>
  </div>
  <div>
    <h2>ChatGPT Response:</h2>
    <p id="response"></p>
  </div>
  <script>
    const sendChat = async () => {
      const message = document.getElementById("message").value;
      const chatGptApiKey = "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"; // ChatGPTのAPIキーを指定

      const endPoint = "https://api.openai.com/v1/chat/completions";
      const modelName = "gpt-3.5-turbo";

      const messages = [
        { role: "system", content: '英語の先生として振る舞ってください。' },
        { role: "assistant", content: "Hello, I'm an English teacher. " },
        { role: "user", content: message }
      ];

      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${chatGptApiKey}`
        },
        body: JSON.stringify({
          model: modelName,
          messages: messages,
          max_tokens: 700
        })
      };

      try {
        const response = await fetch(endPoint, requestOptions);
        const json = await response.json();
        const chatGptResponse = json.choices[0].message.content;
        document.getElementById("response").textContent = chatGptResponse;
      } catch (error) {
        console.error("Error:", error);
      }
    };

    const sendMessageButton = document.getElementById("sendMessage");
    sendMessageButton.addEventListener("click", sendChat);
  </script>
</body>
</html>
