from flask import Flask, render_template, request, redirect
import mysql.connector


app = Flask(__name__)

# MySQL connection setup
connection = mysql.connector.connect(
    host='localhost',  # Ensure this is the correct host        
    user='root',       # Default user for XAMPP
    password='J2107jten#',       # Update if password is set
    database='jmishra' # Ensure this database exists
)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure home.html is in the 'templates' folder

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        feedback = request.form['feedback']
        
        try:
            # Insert data into MySQL
            cursor = connection.cursor()
            cursor.execute("INSERT INTO feedbacks (name, email, feedback) VALUES (%s, %s, %s)", (name, email, feedback))
            connection.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "Database error. Please try again later.", 500
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
