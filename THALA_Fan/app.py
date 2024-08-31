from flask import Flask, render_template, request, redirect, url_for
from models import db, FanClubMember

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fan_club.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        if len(number) == 4 and number.isdigit():
            new_member = FanClubMember(name=name, number=number)
            db.session.add(new_member)
            db.session.commit()
            return redirect(url_for('thank_you'))
        else:
            error = "Please enter the last 4 digits of your number."
            return render_template('index.html', error=error)
    return render_template('index.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

