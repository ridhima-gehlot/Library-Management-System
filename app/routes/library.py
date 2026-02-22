from flask import Blueprint, render_template, redirect, request, url_for, session, flash
from app import db
from app.models import books, members, IssueStatus
from datetime import date

library_bp=Blueprint('library', __name__)

#To go to dashboard
@library_bp.route('/')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    all_memebrs=members.query.all()
    return render_template('dashboard.html')

#To view books
@library_bp.route('/books')
def view_books():
    all_books=books.query.all() #fetches all rows from mysql
    return render_template('books.html', books=all_books)

#To view members
@library_bp.route('/members')
def view_members():
    all_members=members.query.all()
    return render_template('members.html', members=all_members)

#To view the status of the books
@library_bp.route('/issue-status')
def issue_status():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    all_issues=IssueStatus.query.all()

    today=date.today()
    #data is used to collect dictionary in this list to calculate fine
    data=[ ]

    for issue in all_issues:
        fine=0

        #If book not returned yet
        #if issue.book_returned==None:
        days_passed=(today-issue.issued_date).days
        if days_passed>15:
                fine=days_passed-15
                status="Not Returned"

        else:
                fine=0
                status="Returned"

                

        data.append({
            "book_id": issue.book_id,
            "book_name": issue.book_name,
            "member_id": issue.member_id,
            "member_name": issue.member_name,
            "issued_date": issue.issued_date,
            "returning_date": issue.returning_date,
            "book_returned": issue.book_returned,
            "status": issue.book_status,
            "fine":fine
            
        })

    return render_template("issue.html", issues=data,)


#to add members
@library_bp.route('/add_member', methods=["GET", "POST"])
def add_member():
    if request.method=="POST":  
        member_id=request.form.get('member_id')
        member_name=request.form.get('member_name')
        memebr_department=request.form.get('member_department')
        member_semester=request.form.get('member_semester')

        new_members=members(
        member_id=member_id,
        member_name=member_name,
        member_department=memebr_department,
        member_semester=member_semester
        )
        db.session.add(new_members)
        db.session.commit()
        flash("New member added", 'success')
        return redirect(url_for('library.dashboard'))
    return render_template('add-member.html')

#to add new issued book
@library_bp.route('/add_issue', methods=["GET", "POST"])
def add_issue():
    if request.method=="POST":  
        book_id=request.form.get('book_id')
        book_name=request.form.get('book_name')
        member_id=request.form.get('member_id')
        member_name=request.form.get('member_name')
        issued_date=request.form.get('issued_date')
        returning_date=request.form.get('returning_date')
        book_returned=request.form.get('book_returned')
        book_status=request.form.get('book_status')
        member_fine=request.form.get('member_fine')

        new_issue=IssueStatus(
        book_id=book_id,
        book_name=book_name,
        member_id=member_id,
        member_name=member_name,
        issued_date=issued_date,
        returning_date=returning_date,
        book_returned=book_returned,
        book_status=book_status,
        member_fine=member_fine
        )
        db.session.add(new_issue)
        db.session.commit()
        flash("New issue added", 'success')
        return redirect(url_for('library.dashboard'))
    return render_template('add-issue.html')
    