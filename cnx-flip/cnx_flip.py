from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
# Change this config uri later!
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flashcarddb'
db = SQLAlchemy(app)

# # Create our database model
# class Deck(db.Model):
#     __tablename__ = "decks"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), unique=True)
#     cards = relationship("cards")

#     def __init__(self, email):
#         self.title = title

#     def __repr__(self):
#         return '<>' % self.title

class Card(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(100), unique=True)
    definition = db.Column(db.String(500), unique=True)
    
    # parent_id = Column(Integer, ForeignKey('decks.id'))
    
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def __repr__(self):
        return '<>' % (self.term + " " + self.definition)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createCard', methods=['POST'])
def createCard():
    if request.method == 'POST':
        term = request.form['term']
        definition = request.form['definition']
        print term, definition
        # Check if the title dalready exist
        if db.session.query(Card).filter(Card.term == term).count() < 1:
            new_card = Card(term, definition)
            db.session.add(new_card)
            db.session.commit()
        
        # new_card = Card(term, definition)
        # db.session.add(new_card)
        # db.session.commit()
            # change the template name later!!
            return render_template('success.html')
    return render_template('index.html')
if __name__ == '__main__':
    app.debug = True
    app.run()

