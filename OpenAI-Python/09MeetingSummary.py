from openai import OpenAI

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

meeting_text = open("meeting.txt").read()

# ---- OpenAI request ----
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "system",
            "content": "You summarize meetings clearly and professionally."
        },
        {
            "role": "user",
            "content": f"""
Summarize the following meeting.

Provide:
1. Short Summary
2. Key Decisions
3. Action Items

Meeting Text:
{meeting_text}
"""
        }
    ]
)

# ---- output ----
print(response.choices[0].message.content)
