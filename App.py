
from flask import Flask, render_template
from flask_mail import Mail, Message






app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def Home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()