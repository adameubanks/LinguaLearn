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
     [{"text": "You are an English chatbot. Your goal is to speak with me in English. You will correct me if I make mistakes and you will help me express myself in the English language. You will help me ask questions about my hobbies, my family, the weather, etc. and I will answer you. If I make mistakes, you will correct me. We will have a conversation. You will ask me a question after each sentence I say . You will not respond in more than 4 sentences. Here we go! Start by saying hello."}],
         "role": "user"},
     {"parts":
     [{"text": "Hello, I am your English teacher. I am going to ask you some questions so that you can learn to speak English. How are you?"}],
         "role": "model"}]
historie = [{"parts":
        [{"text": "Du bist ein deutscher Chatbot. Dein Ziel ist es, mit mir auf Deutsch zu sprechen. Du wirst mich korrigieren, wenn ich Fehler mache, und du wirst mir helfen, mich in der deutschen Sprache auszudrücken. Du wirst mir helfen, Fragen über meine Hobbys, meine Familie, das Wetter, etc. zu stellen und ich werde dir antworten. Wenn ich Fehler mache, wirst du mich korrigieren. Wir werden ein Gespräch führen. Du wirst mir nach jedem Satz, den ich sage, eine Frage stellen. Du wirst nicht in mehr als 4 Sätzen antworten. Los geht's! Fangen Sie damit an, Hallo zu sagen."}],
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
        except genai.types.generation_types.BlockedPromptException:
            return "¡Eso no es agradable! Intenta decir algo más amable."
        except:
            return "Ups ! Hubo un error. Intenta decir algo más simple."
        
    elif lang == 'fr':
        chat = model.start_chat(history=histoire)
        try:
            response = chat.send_message(msg)
            reponse = response.text.replace("*","")
            return reponse
        except genai.types.generation_types.BlockedPromptException:
            return "C'est pas gentil, ça ! Essayez de dire quelque chose de plus gentil."
        except:
            return "Oups ! Il y a eu une erreur. Essayez de dire quelque chose de plus simple."
    
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