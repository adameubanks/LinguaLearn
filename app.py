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
    return render_template("french.html")

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg') 
    userLang = request.referrer[-2:]
    print(userLang)
    response = gemini_pro.get_response(userText, userLang) 
    return response


if __name__ == '__main__':
    app.run()
