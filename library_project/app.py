from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "library_system_2026"

# Mock Data to simulate a database
books_database = [
    {"id": 1, "title": "Software Engineering", "author": "Ian Sommerville", "type": "book"},
    {"id": 2, "title": "Data Structures", "author": "Narasimha Karumanchi", "type": "book"},
    {"id": 3, "title": "Inception", "author": "Christopher Nolan", "type": "movie"}
]

@app.route('/')
def index():
    """Renders the main search page with the book list."""
    return render_template('index.html', books=books_database)

@app.route('/issue', methods=['POST'])
def issue_book():
    """Handles the book issuance logic."""
    book_id = request.form.get('selected_book')
    
    # Requirement: Validation - User must get a message if none selected
    if not book_id:
        flash("Error: Please make a valid selection of the feature.")
        return redirect(url_for('index'))

    # Find the book details
    book = next((b for b in books_database if b["id"] == int(book_id)), None)
    
    # Requirement: Issue Date cannot be lesser than today
    issue_date = datetime.now().date()
    
    # Requirement: Return Date defaults to 15 days ahead
    return_date = issue_date + timedelta(days=15)
    
    return render_template('issue_details.html', 
                           book=book, 
                           issue_date=issue_date, 
                           return_date=return_date)

@app.route('/return', methods=['POST'])
def return_process():
    """Handles the return process and redirection to Fine Pay."""
    serial_no = request.form.get('serial_no')
    
    # Requirement: Serial No of the book is a mandatory field
    if not serial_no:
        flash("Error: Serial No of the book is a mandatory field.")
        return redirect(url_for('index'))
    
    # Requirement: Redirect to Pay Fine irrespective of whether fine is there or not
    # Logic: Assume fine of $10 for certain serials, else $0
    fine_amount = 10.0 if serial_no == "123" else 0.0
    
    return render_template('pay_fine.html', 
                           serial_no=serial_no, 
                           fine_amount=fine_amount)

@app.route('/confirm_fine', methods=['POST'])
def confirm_fine():
    """Completes the transaction."""
    # Requirement: If pending fine, check box needs to be selected
    fine_paid = request.form.get('fine_paid')
    fine_amt = request.form.get('fine_amt')
    
    if float(fine_amt) > 0 and not fine_paid:
        flash("Error: Paid fine check box needs to be selected for pending fine.")
        return redirect(url_for('index'))
        
    flash("Transaction successfully completed.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Running the development server
    app.run(debug=True)