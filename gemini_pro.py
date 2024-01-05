import google.generativeai as genai

with open('googleapikey.txt', 'r') as f:
    GOOGLE_API_KEY = f.read()
    f.close()

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

historia = [{"parts":
      [{"text": "Eres un chatbot español. Tu objetivo es hablar conmigo en español. Me corregirás si cometo errores y me ayudarás a expresarme en el idioma español. Me ayudarás a hacer preguntas sobre mis aficiones, mi familia, el tiempo, etc. y te responderé. Si me equivoco, me corregirás. Tendremos una conversación. Me harás una pregunta después de cada frase que diga. ¡Vamos! Empezar por saludando."}],
         "role": "user"},
     {"parts":
     [{"text": "Hola, soy tu profesora de español. Te voy a hacer unas preguntas para que aprendas a hablar español. ¿Cómo estás?"}],
         "role": "model"}]
histoire = [{"parts":
    [{"text": "Vous êtes un chatbot français. Votre objectif est de parler avec moi en français. Vous allez me corriger si je fais des erreurs et vous allez m'aider à m'exprimer dans la langue française. Vous allez me poser des questions sur mes loisirs, ma famille, la méteo, etc. et je vais vous répondre. Si je fais des erreurs, vous allez me corriger. On va tenir une conversation. Vous allez me poser une question après chaque phrase que je dis. C'est parti ! Commencez par me dire bonjour."}], 
        "role": "user"},
    {"parts": 
    [{"text": "Bonjour, je suis votre professeur de français. Je vais vous poser des questions pour que vous puissiez apprendre à parler français. Comment allez-vous ?"}],
        "role": "model"}]


def get_response(msg, lang):
    if lang == 'es':
        chat.set_chat_lang('es')
        chat = model.start_chat(history=historia)
        try:
            response = chat.send_message(msg)
            return response.text
        except genai.types.generation_types.BlockedPromptException:
            return "¡Eso no es agradable! Intenta decir algo más amable."
        except:
            return "Ups ! Hubo un error. Intente decir algo más simple."
        
    elif lang == 'fr':
        chat.set_chat_lang('fr')
        chat = model.start_chat(history=histoire)
        try:
            response = chat.send_message(msg)
            return response.text
        except genai.types.generation_types.BlockedPromptException:
            return "C'est pas gentil, ça ! Essayez de dire quelque chose de plus gentil."
        except:
            return "Oups ! Il y a eu une erreur. Essayez de dire quelque chose de plus simple."
        
    elif lang == 'de':
        chat.set_chat_lang('de')