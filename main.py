import flask
from flask import Flask, render_template, request, flash

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

        name = request.form.get('fname')
        name = name.upper()
        enrollment = request.form.get('enrollment')
        if enrollment == 'DME/5442' and name == 'Jay'.upper():
            message = True
        else:
            message = 'NotTrue'
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
