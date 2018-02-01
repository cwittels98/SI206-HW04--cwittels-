import random

def ask_question():
    user_input = ""
    while user_input != exit:
        user_input = input("What is your question?")
        if user_input == "exit":
            break
        if user_input[-1] != "?":
            print ("Sorry, I can only answer qustions. Please ask another question, or write "exit" to quit.")
        else:
            lst_of_resposes = ["It is certain", "It is decidedly so, Without a doubt",
                               "Yes definitely", "You may rely on it", "As I see it", "yes", "Most likely", "Outlook good", "Yes",
                               "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now"
                               "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
            answer = random.choice(lst_of_responses)
            print answer
