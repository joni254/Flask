
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Secret Key'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mwangi:.D3v3l0p3r!@localhost/Employee'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    department = db.Column(db.String(100))

    def __init__(self, name, email, department):
        self.name = name
        self.email = email
        self.department = department


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def Home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
    