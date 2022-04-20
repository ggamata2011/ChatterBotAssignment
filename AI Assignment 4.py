#Assignment 4
#Guiller Gamata
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement

#For use in learning feedback to help the bot learn
def feedback():

    feed = input()

    if 'yes' in feed.lower():
        return True
    elif 'no' in feed.lower():
        return False
    else:
        print('Enter "Yes" or "No"')
        return feedback()
#End function definition

# Create a new chatBot
chatbot = ChatBot('Assistant',logic_adapters =[
    { 'import_path':'chatterbot.logic.BestMatch',
      'default_response': 'I am not sure what you mean,I provide directions and general information only',
      'maximum_similarity_threshold': 0.50}],
      storage_adapter= 'chatterbot.storage.SQLStorageAdapter'
    )    



CorpusTrainer = ChatterBotCorpusTrainer(chatbot)
CorpusTrainer.train("./Greetings-Directions.yml","./General-Information.yml")

print("Welcome to St.Rose Hospital main terminal, How may I help you?\n")

# Get a response to the input text 'I would like to book a flight.'
while True:
    try:
        print("You:")
        Query = input()
        response = chatbot.get_response(Query)
        print("Assistant:")
        print(response)

        #Valid Response checker code
        #print('\nIs this a valid response?')
        #if feedback() is False:
        #    print('please input the correct response')
        #    text = input()
        #    correct_response = Statement(text)
        #    chatbot.learn_response(correct_response, Query)
        #    print('Responses added to bot!\n')
        #    print("\n")
        #Valid Response Checker done

    except(KeyboardInterrupt, EOFError, SystemExit):
        break




    
