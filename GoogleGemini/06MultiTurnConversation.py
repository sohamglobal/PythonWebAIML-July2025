from google import genai

client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash")

response = chat.send_message("My team lost the match yesterday. How do you think I am feeling?")
print(response.text)

response = chat.send_message("What can I do to feel better?")
print(response.text)

for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)