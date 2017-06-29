from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

# Create our database model
class Deck(db.Model):
    __tablename__ = "decks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    cards = relationship("cards")

    def __init__(self, email):
        self.title = title

    def __repr__(self):
        return % self.title

class Card(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(100), unique=True)
    definition = db.Column(db.String(500), unique=True)
    
    parent_id = Column(Integer, ForeignKey('decks.id'))
    
    def __init__(self, term, definition):
        self.definition = term

    def __repr__(self):
        return % (self.term + " " + self.definition)