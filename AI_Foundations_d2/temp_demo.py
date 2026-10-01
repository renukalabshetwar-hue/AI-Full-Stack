from ollama import chat
for temp in [0,0.7,1,5]:
    print(f"temperature: {temp}")
    for run in range(3):
        response=chat(
            model="llama3.2",
            messages=[
                {"role": "user", "content": "what are the 7 colors in a rainbow?"},
            ],
            options={
                "temperature": temp
            },
            #temperature=temp
        )
    print(f"Run {run + 1}: {response.message.content}")
    print()
    