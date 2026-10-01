from ollama import chat

prompt = "I'm late to class. Give me ONE short excuse in ONE sentence."

for temp in [0, 0.7, 1.5]:
    print(" " * 60)
    print(f"TEMPERATURE: {temp}")
    print(" " * 60)

    for run in range(3):
        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": temp
            }
        )

        print(f"Run {run + 1}: {response.message.content.strip()}")
