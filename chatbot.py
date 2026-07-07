# ==========================================================
# DecodeLabs Artificial Intelligence Internship
# Project 1 - Rule-Based AI Chatbot
# Rule-Based AI using if-elif-else
# ==========================================================

print("=" * 60)
print("🤖 Welcome to the Rule-Based AI Chatbot")
print("=" * 60)
print("Hello! I am RuleBot, your virtual assistant.")
print("Type 'help' to see the available commands.")
print("Type 'bye' anytime to exit.\n")

while True:

    user = input("You : ").strip().lower()

    # ------------------ Greetings ------------------

    if user in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:
        print("Bot : Hello! Nice to meet you.")

    # ------------------ About Bot ------------------

    elif user in ["what is your name", "your name", "who are you"]:
        print("Bot : My name is RuleBot, a simple rule-based AI chatbot.")

    elif user in ["who created you", "who made you", "who developed you"]:
        print("Bot : I was created using Python with rule-based logic.")

    elif user in ["what can you do", "what do you do", "what are your features"]:
        print("Bot : I can answer predefined questions using if-else logic.")

    elif user in ["how are you", "how are you doing", "are you fine"]:
        print("Bot : I am doing great! Thanks for asking.")

    # ------------------ AI ------------------

    elif user in ["ai", "what is ai", "what is artificial intelligence"]:
        print("Bot : Artificial Intelligence (AI) enables machines to perform tasks that usually require human intelligence.")

    elif user in ["machine learning", "what is machine learning", "define machine learning"]:
        print("Bot : Machine Learning is a branch of AI that allows computers to learn from data.")

    elif user in ["deep learning", "what is deep learning", "define deep learning"]:
        print("Bot : Deep Learning is a subset of Machine Learning that uses neural networks.")

    elif user in ["chatbot", "what is chatbot", "define chatbot"]:
        print("Bot : A chatbot is a program that interacts with users through conversation.")

    # ------------------ Python ------------------

    elif user in ["python", "what is python", "define python"]:
        print("Bot : Python is a popular programming language used in AI, web development, automation, and data science.")

    elif user in ["programming", "what is programming", "define programming"]:
        print("Bot : Programming is the process of writing instructions for computers.")

    # ------------------ Data Science ------------------

    elif user in ["data science", "what is data science", "define data science"]:
        print("Bot : Data Science is the field of analyzing data to gain meaningful insights.")

    # ------------------ Internship ------------------

    elif user in ["internship", "project", "project 1"]:
        print("Bot : This chatbot was developed as Project 1 of the DecodeLabs AI Internship.")

    # ------------------ General ------------------

    elif user in ["thank you", "thanks", "thankyou"]:
        print("Bot : You're welcome!")

    elif user in ["date", "today's date", "what is today's date"]:
        print("Bot : Sorry, I cannot provide the current date.")

    elif user in ["time", "current time", "what is the time"]:
        print("Bot : Sorry, I cannot provide the current time.")

    elif user in ["joke", "tell me a joke", "make me laugh"]:
        print("Bot : Why do programmers prefer Python? Because it's easy to learn and fun to code!")

    # ------------------ Help ------------------

    elif user == "help":

        print("\n========== Available Commands ==========")
        print("• hello / hi / hey")
        print("• how are you")
        print("• what is your name")
        print("• who created you")
        print("• what can you do")
        print("• what is AI")
        print("• what is Python")
        print("• what is Machine Learning")
        print("• what is Deep Learning")
        print("• what is Data Science")
        print("• what is Programming")
        print("• chatbot")
        print("• internship")
        print("• project")
        print("• joke")
        print("• date")
        print("• time")
        print("• thank you")
        print("• bye")
        print("========================================\n")

    # ------------------ Exit ------------------

    elif user in ["bye", "goodbye", "exit", "quit"]:
        print("Bot : Thank you for chatting with me.")
        print("Bot : Have a wonderful day! 👋")
        break

    # ------------------ Unknown ------------------

    else:
        print("Bot : Sorry, I don't understand that.")
        print("Bot : Type 'help' to see the available commands.")