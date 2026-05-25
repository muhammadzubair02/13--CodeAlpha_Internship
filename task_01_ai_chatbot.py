def chatbot():

    print("Welcome! to Chatbot.")

    user_input = ""

    while user_input != "bye":

        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "hi":
            print("Bot: Hello!")

        elif user_input == "how are you?":
            print("Bot: I'm fine! Thanks, and what about you?")

        elif "also good" in user_input:
            print("Bot: Nice to meet you.")
        elif user_input == "nice to meet you too.":
            print("Bot: nice!, what about today plan?")
        elif user_input == "nothing important only complete my codealpha assignment.":
            print("Bot: That's Great!, do first")

        elif user_input == "ok bye":
            break

        else:
            print("Bot: It's a rule-based chatbot and accepts only predefined replies. Thanks!")

    print("Bot: Goodbye!")


chatbot()