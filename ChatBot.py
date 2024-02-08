import nltk
from nltk.chat.util import Chat, reflections

# Define patterns for the chatbot to recognize and respond to
patterns = [
    (r'.*I am (depressed|sad|unhappy).*',
     ['I\'m sorry to hear that. Can you tell me more about what\'s been bothering you?',
      'It\'s important to talk about your feelings. What\'s been on your mind?']),
    (r'.*I feel (anxious|stressed|worried|lonely).*',
     ['Anxiety can be tough to deal with. What specifically has been causing you to feel this way?',
      'Let\'s try to work through your feelings of stress together. What\'s been happening?']),
    (r'.*(I hate|I dislike) (myself|life).*',
     ['It sounds like you\'re going through a tough time. Can you share more about what\'s been going on?',
      'Remember, it\'s okay to feel this way, but there\'s always hope for things to improve. What\'s been troubling you?']),
    (r'.*I (need|want) (help|advice).*',
     ['I\'m here to help. What do you need advice or assistance with?',
      'You\'re not alone. Feel free to share what\'s been on your mind, and we can work through it together.']),
    (r'.*',
     ["I see.", "Can you tell me more?", "How does that make you feel?", "Is there anyone you cna talk to about this?"])  # Default response
]

# Create a chatbot using NLTK's Chat class
counselor_chatbot = Chat(patterns, reflections)

# Start a conversation with the chatbot
print("Counselor Chatbot: Hello, I'm here to listen and offer support. You can share anything with me.")
print("Counselor Chatbot: If you want to exit, simply type 'exit'.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Counselor Chatbot: Thank you for talking with me. Take care.")
        break
    else:
        print("Counselor Chatbot:", counselor_chatbot.respond(user_input))
