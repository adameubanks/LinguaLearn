from flask import Flask, request, render_template
import gemini_pro

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/es")
def spanish(): 
    return render_template("spanish.html")

@app.route("/fr")
def french(): 
    return render_template("french.html")

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = gemini_pro.get_response(userText) 
    return response


if __name__ == '__main__':
    app.run()
