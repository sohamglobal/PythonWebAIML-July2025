from openai import OpenAI

# Contact SohamGlobal 73919 66656 for API key if you don't have one
client = OpenAI(api_key="your_api_key_here")

code_snippet = """
List<String> lst=new ArrayList<>();
lst.add("Apple");
lst.add("Banana");
lst.stream().forEach(System.out::println);
"""

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role":"system","content":"You are a helpful programming tutor."},
        {"role":"user","content":f"Explain this code:\n{code_snippet}"}
    ],
)

print(response.choices[0].message.content)
