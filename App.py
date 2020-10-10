
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



@app.route('/', methods=['GET'],)
def Home():

    all_data = Employee.query.all()
    return render_template("index.html", E = all_data)

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

@app.route('/update', methods = ['GET','POST'])
def Update():
    if request.method == 'POST':
        the_data = Employee.query.get(request.form.get('id'))

        the_data.name = request.form['name']
        the_data.email = request.form['email']
        the_data.department = request.form['department']

        db.session.commit()
        flash('Record updated successfully')
        return redirect(url_for('Home'))

@app.route('/delete/<id>/', methods=['GET','POST'])
def delete(id):
    del_data = Employee.query.get(id)
    db.session.delete(del_data)
    db.session.commit()
    flash('Data deleted successfully')

    return redirect(url_for('Home'))


if __name__ == "__main__":
    app.run(debug=True)
    