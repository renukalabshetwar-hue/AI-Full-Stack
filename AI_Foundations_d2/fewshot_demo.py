from ollama import chat
messages=[
    {"role": "system","content": "Classify the sentiment as positive, negative,neutral.Reply with one word"},

    {"role":"user","content":"Great Movie!"},
    {"role":"user","content":"positive"},

    {"role":"user","content":"waste of money"},
    {"role":"user","content":"negative"},

    {"role":"user","content":"It was okay"},
    {"role":"user","content":"neutral"},
]
response=chat(
    model="llama3.2",
    messages=messages
)
print(response.message.content)
