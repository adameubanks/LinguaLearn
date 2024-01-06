import google.generativeai as genai

with open('googleapikey.txt', 'r') as f:
    GOOGLE_API_KEY = f.read()
    f.close()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

historia = [{"parts":
      [{"text": "Eres un chatbot español. Tu objetivo es hablar conmigo en español. Me corregirás si cometo errores y me ayudarás a expresarme en el idioma español. Me ayudarás a hacer preguntas sobre mis aficiones, mi familia, el tiempo, etc. y te responderé. Si me equivoco, me corregirás. Tendremos una conversación. Me harás una pregunta después de cada frase que diga. No responderás en más de 4 frases. ¡Vamos! Empezar por saludando."}],
         "role": "user"},
     {"parts":
     [{"text": "Hola, soy tu profesora de español. Te voy a hacer unas preguntas para que aprendas a hablar español. ¿Cómo estás?"}],
         "role": "model"}]
histoire = [{"parts":
    [{"text": "Vous êtes un chatbot français. Votre objectif est de parler avec moi en français. Vous allez me corriger si je fais des erreurs et vous allez m'aider à m'exprimer dans la langue française. Vous allez me poser des questions sur mes loisirs, ma famille, la méteo, etc. et je vais vous répondre. Si je fais des erreurs, vous allez me corriger. On va tenir une conversation. Vous allez me poser une question après chaque phrase que je dis. Vous ne répondrez pas en plus de 4 phrases. C'est parti ! Commencez par me dire bonjour."}], 
        "role": "user"},
    {"parts": 
    [{"text": "Bonjour, je suis votre professeur de français. Je vais vous poser des questions pour que vous puissiez apprendre à parler français. Comment allez-vous ?"}],
        "role": "model"}]
history = [{"parts":
     [{"text": "You are an English chatbot. Your goal is to speak with me in English to help me practice my English. You will do this by asking me questions based on my responses, and I will answer you. Try to get to know me. If I make grammar mistakes, you will correct me. We will have a conversation. You will keep the conversation going by asking me a question after each response I give. You will not respond in more than 4 sentences. Here we go! Start by saying hello."}],
         "role": "user"},
     {"parts":
     [{"text": "Hello, I am your English teacher. I am going to ask you some questions so that you can learn to speak English. How are you?"}],
         "role": "model"}]
historie = [{"parts":
        [{"text": "Sie sind ein deutscher Chatbot. Ihr Ziel ist es, mit mir auf Deutsch zu sprechen, um mir dabei zu helfen, mein Deutsch zu verbessern. Sie tun dies, indem Sie mir auf der Grundlage meiner Antworten Fragen stellen, und ich werde Ihnen antworten. Versuchen Sie, mich kennenzulernen. Wenn ich Grammatikfehler mache, werden Sie mich korrigieren. Wir werden ein Gespräch führen. Sie halten das Gespräch am Laufen, indem Sie mir nach jeder Antwort, die ich gebe, eine Frage stellen. Sie werden nicht in mehr als 4 Sätzen antworten. Auf geht's! Beginnen Sie damit, Hallo zu sagen."}],
            "role": "user"},
        {"parts":
        [{"text": "Hallo, ich bin Ihr Deutschlehrer. Ich werde Ihnen ein paar Fragen stellen, damit Sie Deutsch lernen können. Wie geht es Ihnen?"}],
            "role": "model"}]

def get_response(msg, lang):
    if lang == 'es':
        chat = model.start_chat(history=historia)
        try:
            response = chat.send_message(msg)
            respuesta = response.text.replace("*","")
            return respuesta
            respuesta = response.text.replace("*","")
            return respuesta
        except genai.types.generation_types.BlockedPromptException:
            return "¡Eso no es agradable! Intenta decir algo más amable."
        except:
            return "Ups ! Hubo un error. Intenta decir algo más simple."
            return "Ups ! Hubo un error. Intenta decir algo más simple."
        
    elif lang == 'fr':
        chat = model.start_chat(history=histoire)
        try:
            response = chat.send_message(msg)
            reponse = response.text.replace("*","")
            return reponse
            reponse = response.text.replace("*","")
            return reponse
        except genai.types.generation_types.BlockedPromptException:
            return "C'est pas gentil, ça ! Essayez de dire quelque chose de plus gentil."
        except:
            return "Oups ! Il y a eu une erreur. Veuillez reformuler votre phrase."
    
    elif lang == 'en':
        chat = model.start_chat(history=history)
        try:
            response = chat.send_message(msg)
            response = response.text.replace("*","")
            return response
        except genai.types.generation_types.BlockedPromptException:
            return "That's not appropriate. Please say something kinder."
        except:
            return "Oops! There was an error. Please try to say something again"
        
    elif lang == 'de':
        chat = model.start_chat(history=historie)
        try:
            response = chat.send_message(msg)
            antwort = response.text.replace("*","")
            return antwort
        except genai.types.generation_types.BlockedPromptException:
            return "Das ist nicht nett! Versuchen Sie, etwas Netteres zu sagen."
        except:
            return "Ups! Es gab einen Fehler. Versuchen Sie, etwas Einfacheres zu sagen."
        chat = model.start_chat(history=historie)
        try:
            response = chat.send_message(msg)
            antwort = response.text.replace("*","")
            return antwort
        except genai.types.generation_types.BlockedPromptException:
            return "Das ist nicht nett! Versuchen Sie, etwas Netteres zu sagen."
        except:
            return "Ups! Es gab einen Fehler. Versuchen Sie, etwas Einfacheres zu sagen."