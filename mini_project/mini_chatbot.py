from ollama import chat
system_msg = " you are a friendly person.answer  warlmy.answer in one sentence."
history=[{"role": "user", "content": system_msg},]
question_counter=0
print("****WELCOME BACK😊****")
while True:
    question=input("YOU: ")
    if question =="":
        print("Alexa🤖: Please enter a question.🙋‍♀️")
        continue
    if question.lower().strip() == 'exit' or question.lower().strip() == 'quit':
        print("Alexa🤖: Exiting the chatbot. Goodbye!🙋‍♀️")
        print(f"you asked {question_counter} questions in this session..Good job🤔")
        break
    if question.lower().strip()=="/history":
        print("-------------------your conversation so far---------------")
        if len(history) <2:
            print("nothing here so far !")
        for msg in history[1:]:
            if msg["role"]=="user":
                speaker="you"
            else:
                speaker ="Alexa"
            print(f"{speaker}: {msg['content']}")
        print("----------------------------------")
        print()
        continue
    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_msg}]
        print("your chat history has been cleared.start a fresh convo!")
        print()
        continue

    if question.lower().strip()=="/help":
        print("----- List of available commands -----")
        print ("/history - displays chat history")
        print("/clear - wipes away your chat history")
        print ("exit - quits your chat window")
        print ("/help - displays this list")
        print("----------------------------------")
        print()
        continue

    history.append({"role":"user","content":question})
    question_counter+=1
    try:

        response = chat(
            model="llama3.2",
            messages=history
            
        )
        
        reply=response["message"]["content"]
        history.append({"role":"assistant","content":reply})
        print(f"alexa:{reply}")
        print()
    except Exception as e:
        print("unkonwn error occurred ,Is ollama running?🤔")


