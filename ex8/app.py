from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/open')
@app.route('/')
def openPage():
    return render_template('cv.html')

@app.route('/contact')
def Contact():
    return render_template('Contact.html')

@app.route('/UserList')
def UserList():
    return render_template('UserList.html')

@app.route('/Assignment8')
def Assignment8():
    return render_template('Assignment8.html', hobby2='Pilatis', name="Danna", hobbies=['Cooking','TV','Dogs'])

@app.route('/AAssignment8')
def AAssignment8():
    return render_template('AAssignment8.html', hobby2='Pilatis', name="Danna", hobbies=['Cooking','TV','Dogs'])


if __name__ == '__main__':
    app.run(debug=True)
