from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FanClubMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(4), nullable=False)

