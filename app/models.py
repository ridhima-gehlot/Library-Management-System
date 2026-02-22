from app import db
from datetime import date

class books(db.Model):
    __tablename__="books"
    book_id=db.Column(db.Integer, primary_key=True)
    book_name=db.Column(db.String(100), nullable=False)
    total_copies=db.Column(db.Integer, nullable=False)

class members(db.Model):
    __tablename__="members"
    member_id=db.Column(db.Integer, primary_key=True)
    member_name=db.Column(db.String(100), nullable=False)
    member_department=db.Column(db.String(100), nullable=False)
    member_semester=db.Column(db.Integer, nullable=False)

class IssueStatus(db.Model):
    __tablename__="issue_status"
    book_id=db.Column(db.Integer, nullable=False)
    book_name=db.Column(db.String(100), nullable=False)
    member_id=db.Column(db.Integer, primary_key=True, nullable=False)
    member_name=db.Column(db.String(100), nullable=False)
    issued_date=db.Column(db.Date, nullable=False)
    returning_date=db.Column(db.Date, nullable=False)
    book_returned=db.Column(db.Date, nullable=True)
    book_status=db.Column(db.String(20), nullable=False)
    member_fine=db.Column(db.Integer)
