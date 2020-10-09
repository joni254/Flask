
from flask import Flask, render_template, request, redirect, url_for,flash
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



@app.route('/', methods=['GET'])
def Home():
    return render_template("index.html")

@app.route('/insert', methods = ['POST'])
def Insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']


        my_data = Employee(name, email,department)
        db.session.add(my_data)
        db.session.commit()
        flash('Record inserted successfully')

        return redirect(url_for('Home'))

if __name__ == "__main__":
    app.run(debug=True)
    