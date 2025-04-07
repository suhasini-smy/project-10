
### Step 2: chatbot.py (NLP logic using spaCy or Transformers)

# You can switch to HuggingFace BERT here if needed
import spacy

# Load small English model
nlp = spacy.load("en_core_web_sm")

responses = {
    "greeting": ["Hi there! How can I help you today?", "Hello! What can I do for you?"],
    "goodbye": ["Goodbye! Have a great day.", "See you later!"],
    "help": ["I'm here to help. Ask me anything about your account, orders, or issues."],
}

def get_intent(user_input):
    doc = nlp(user_input.lower())
    if any(token.lemma_ in ["hi", "hello", "hey"] for token in doc):
        return "greeting"
    elif any(token.lemma_ in ["bye", "goodbye"] for token in doc):
        return "goodbye"
    elif "help" in user_input:
        return "help"
    else:
        return "default"

def get_bot_response(user_input):
    intent = get_intent(user_input)
    if intent in responses:
        return responses[intent][0]
    else:
        return "I'm not sure how to help with that yet, but I'm learning!"

