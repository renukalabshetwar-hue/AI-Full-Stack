from ollama import chat
roles = [
    "you are a strict math teacher. Answer is one line"
    "you are a 10 year old. Answer accordingly.Answer in one line",
    "you are dancer. Answer accordingly in 1 line"
]
for role in roles:
    response=chat(
        model="llama3.2",
            messages=[
                {
                    "role" : "system",
                    "content" : role
                },
                {
                    "role": "user",
                    "content": "what are the ? colors in a rainbow? Answer in one line."
                }
            ]
        )
    print(f"role :{role}")
    print(response.message.content)
    print()
    
    