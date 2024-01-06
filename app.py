from flask import Flask, request, render_template
import gemini_pro

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/es")
def spanish(): 
    return render_template("chat.html", lang_title="Español", lang_code="es-US", 
                           intro_message="Hola, soy tu profesora de español. ¿Cómo estás?", placeholder="Escribe tu mensaje aquí...")

@app.route("/fr")
def french(): 
    return render_template("chat.html", lang_title="Français", lang_code="fr-FR", 
                        intro_message="Bonjour, je suis votre professeur de français. Comment allez-vous aujourd'hui ?", placeholder="Ecrire votre message...")

@app.route("/en")
def english(): 
    return render_template("chat.html", lang_title="English", lang_code="en-US", 
                        intro_message="Hello, I am your English teacher. How are you doing today?", placeholder="Write your message here...")

@app.route("/de")
def german(): 
    return render_template("chat.html", lang_title="Deutsch", lang_code="de-DE", 
                        intro_message="Hallo, ich bin Ihr Deutschlehrer. Wie geht es Ihnen?", placeholder="Schreibe deine Nachricht hier...")

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg') 
    userLang = request.referrer[-2:]
    print(userLang)
    response = gemini_pro.get_response(userText, userLang) 
    return response


if __name__ == '__main__':
    app.run()
