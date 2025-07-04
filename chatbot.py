# Advanced Rule-Based Chatbot - Task 8

import datetime

print(" ChatBuddy: Hi! I'm ChatBuddy. Ask me anything, or type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if any(greet in user_input for greet in ["hello", "hi", "hey"]):
        print("ChatBuddy: Hello! How can I help you today?")
    elif "how are you" in user_input:
        print("ChatBuddy: I'm doing great, thank you! Hope you're doing well too.")
    elif "your name" in user_input:
        print("ChatBuddy: I'm ChatBuddy, your friendly chatbot assistant.")
    elif "time" in user_input:
        now = datetime.datetime.now()
        print(f"ChatBuddy: The current time is {now.strftime('%I:%M %p')}.")
    elif "date" in user_input:
        today = datetime.date.today()
        print(f"ChatBuddy: Today's date is {today.strftime('%B %d, %Y')}.")
    elif "what can you do" in user_input or "features" in user_input:
        print("ChatBuddy: I can chat with you, tell the time and date, and answer simple questions!")
    elif "internship" in user_input:
        print("ChatBuddy: Internships are a great way to gain experience. Keep learning and building projects!")
    elif "skills" in user_input:
        print("ChatBuddy: Python, HTML, CSS, Flask, basic chatbot design, and GitHub are good skills to have.")
    elif "thank you" in user_input:
        print("ChatBuddy: You're welcome! ")
    elif "bye" in user_input or "exit" in user_input:
        print("ChatBuddy: Bye! Have a great day ahead! ")
        break
    else:
        print("ChatBuddy: Sorry, I didn't understand that. Try asking something else!")