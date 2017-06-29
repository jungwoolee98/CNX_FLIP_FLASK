from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    children = relationship("Child")

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

class Child(db.Model):
    __tablename__ = "children"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    
    parent_id = Column(Integer, ForeignKey('users.id'))
    
    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['term']
        # Check that email does not already exist (not a great query, but works)
        if db.session.query(User).filter(User.email == email).count() < 1:
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
        
        email2 = request.form['term']
        # Check that email does not already exist (not a great query, but works)
        if db.session.query(Child).filter(Child.email == email2).count() < 1:
            reg = Child(email2)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()