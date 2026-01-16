from openai import OpenAI

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

story_start = """
I prisoner found himself in a dark, damp cell. The only light came from a small 
window high above him. He had to find a way out. He decided to explore the cell,
looking for any weaknesses in the walls or floor. After hours of searching, 
he found a loose stone in the wall... 
"""

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "system",
            "content": "You are a creative story writer."
        },
        {
            "role": "user",
            "content": f"""
Continue the story below and provide THREE different endings.
Keep each ending short and imaginative.

Story start:
{story_start}
"""
        }
    ],
    temperature=0.9   # higher creativity
)

print(response.choices[0].message.content)
