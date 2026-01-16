from openai import OpenAI

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

# ---- context memory ----
conversation = [
    {"role": "system", "content": "You are a helpful, friendly chatbot."}
]

print("SohamGlobal Chatbot started (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # add user message to memory
    conversation.append({"role": "user", "content": user_input})

    # call OpenAI
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=conversation
    )

    bot_reply = response.choices[0].message.content

    # add bot reply to memory
    conversation.append({"role": "assistant", "content": bot_reply})

    print("Bot:", bot_reply, "\n")
