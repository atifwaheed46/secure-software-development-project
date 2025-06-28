from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
from datetime import timedelta  #  Import timedelta

app = Flask(__name__)
app.secret_key = 'ssdd_demo'

#  Set session timeout to 10 minutes
app.permanent_session_lifetime = timedelta(minutes=10)

# In-memory "database"
students = []
users = {}  # {username: password}

# ----------------- Auth Routes -----------------

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash("Username and password are required.")
            return redirect('/register')

        # ✅ Strong password check: min 8 chars, uppercase, lowercase, digit, special char
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(pattern, password):
            flash("Password must be at least 8 characters and include uppercase, lowercase, number, and special character.")
            return redirect('/register')

        if username in users:
            flash("Username already exists.")
            return redirect('/register')

        users[username] = password
        flash("Registered successfully. Please log in.")
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['user'] = username
            session.permanent = True  # ✅ Ensure session respects timeout
            flash("Logged in successfully.")
            return redirect('/')
        else:
            flash("Invalid credentials.")
            return redirect('/login')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out.")
    return redirect('/login')

# ----------------- Protected Student CRUD -----------------

def login_required(route):
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            flash("Please log in to continue.")
            return redirect('/login')
        return route(*args, **kwargs)
    wrapper.__name__ = route.__name__
    return wrapper

@app.route('/')
@login_required
def index():
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']

        if not re.match(r'^[A-Za-z ]+$', name):
            flash('Name must contain only alphabets.')
            return redirect('/add')
        if not re.match(r'^\S+@\S+\.\S+$', email):
            flash('Invalid email format.')
            return redirect('/add')
        if not age.isdigit():
            flash('Age must be numeric.')
            return redirect('/add')

        students.append({'name': name, 'email': email, 'age': age})
        flash('Student added successfully!')
        return redirect('/')

    return render_template('form.html', action='Add', student=None)

@app.route('/delete/<int:student_id>')
@login_required
def delete_student(student_id):
    try:
        students.pop(student_id)
        flash('Student deleted.')
    except IndexError:
        flash('Invalid student ID.')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')