#Assignment 4
#Guiller Gamata
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a new chatBot
chatbot = ChatBot('Assistant')

CorpusTrainer = ChatterBotCorpusTrainer(chatbot)
#ListTrain.train("Hello There")
CorpusTrainer.train("./Custom Conversation.yml")
#"./CustomConversation.json"
#"chatterbot.corpus.english","./Custom Conversation.yml",


# Get a response to the input text 'I would like to book a flight.'
while True:
    try:
        Query = input()
        response = chatbot.get_response(Query)
        print(response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break


#Export Data to json file
#CorpusTrainer.export_for_training('./CustomConversation.json')
