from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, flash
from fetch_info import get_codehs_info
import os
import shutil

app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('home.html')

# Define the PDF route
@app.route('/pdf')
def pdf():
    return render_template('pdf.html')

# Define the Code HS route
@app.route('/codehs', methods=['GET', 'POST'])
def codehs():

    # Delete the screenshot if it exists
    file_path = "static/scrn/screenshot.png"

    if os.path.exists(file_path):
        os.unlink(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"{file_path} does not exist.")


    # Copy the 'waiting' png as 'screenshot.png'
    shutil.copyfile("static/scrn/waiting.png", "static/scrn/screenshot.png")


    if request.method == 'POST':
        # Get the student number and exercise number

        student_number = request.form['student_number']
        exercise_number = request.form['exercise_number']
        get_codehs_info(student_number, exercise_number)

    return render_template('codehs.html')

# Define the Project STEM route
@app.route('/prjstem')
def prjstem():
    return render_template('prjstem.html')


# Define the reports route
@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True)
