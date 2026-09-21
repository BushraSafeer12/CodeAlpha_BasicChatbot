def chatbot():
    replies = [
        'Hi! How can I help you?', 'Hello','I am Fine', 'I am a python chatbot', 'Welcome',
        'I can answer some basic questions and chat with you!','Good Morning', 'Good afternoon','Good Night',
        'Goodbye!', 'Good Evening','Sorry I dont understand' ]
    print("Welcome to the Chatbot!")
    print()

    while True:
        user = input("You: ").lower()
        if user == 'hi':
            print('Bot: ', replies[0])
            print()
        elif user == 'hello':
            print('Bot: ', replies[1])
            print()
        elif user == 'how are you?':
            print('Bot: ', replies[2])
            print()
        elif user == 'what is your name?':
            print('Bot: ', replies[3])
            print()
        elif user == 'thanks':
            print('Bot: ', replies[4])
            print()
        elif user == 'what can you do?':
            print('Bot: ', replies[5])
            print()
        elif user == 'good morning':
            print('Bot: ', replies[6])
            print()
        elif user == 'good afternoon':
            print('Bot: ', replies[7])
            print()
        elif user == 'good night':
            print('Bot: ', replies[8])
            print()
        elif user == 'bye':
            print('Bot: ', replies[9])
            print()
            break
        elif user == 'good evening':
            print('Bot: ', replies[10])
            print()
        else:
            print('Bot: ', replies[11])
            print()
chatbot()