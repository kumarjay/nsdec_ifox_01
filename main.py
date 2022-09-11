import csv

import flask
from flask import Flask, render_template, request, flash
import pandas as pd
from test_csv import get_name_enrollment
import logging, datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/enrollment', methods=['GET', 'POST'])
def enrollment():
    message = False
    name= False
    if flask.request.method == 'POST':
        timenow = datetime.datetime.now()
        logging.root.setLevel(logging.WARNING)
        logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s — %(levelname)s - %(message)s')

        name = request.form.get('fname')
        name = name.upper()
        enrollment = request.form.get('enrollment')
        entry = get_name_enrollment(name, enrollment)
        logging.info('hellloooooo')
        with open('users.csv', 'a', newline='') as f:
            f = csv.writer(f)
            if entry:
                message = True
                f.writerow([f'{timenow} - INFO - {name} checked their status'])
                logging.warning(f'{name} checked their status')
            else:
                message = 'NotTrue'
                f.writerow([f'{timenow} - WARNING - {name} - {enrollment} checked'])
                logging.error(f'{name} - {enrollment} checked')
    return render_template('enrollment.html', message=message, name=name)


@app.route('/enrollment_action', methods=['GET', 'POST'])
def enrollment_action():
    message = False
    name = request.form.get('fname')
    enrollment = request.form.get('enrollment')
    if enrollment == 'DME/5442':
        message = True
    else:
        message = 'NotTrue'

    return render_template('enrollment.html', message=message)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/courses', methods=['GET', 'POST'])
def courses():
    return render_template('courses.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
