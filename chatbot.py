def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but thanks for asking!")
        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot 1.0, your virtual assistant.")
        elif "help" in user_input:
            print("Chatbot: Sure, I can help! Ask me about the weather, time, or just say hi.")
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        elif "weather" in user_input:
            print("Chatbot: I can't fetch real-time weather, but I hope it's sunny where you are!")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you try asking something else?")


chatbot()
