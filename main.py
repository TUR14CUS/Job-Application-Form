from flask import Flask, render_template, request, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret-key" # You should change this
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" # You should change this
app.config["MAIL_SERVER"] = "smtp.gmail.com" # You should change this
app.config["MAIL_PORT"] = 465 # You should change this
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "email" # You should change this
app.config["MAIL_PASSWORD"] = "password" # You should change this

db = SQLAlchemy(app)

mail = Mail(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    date = db.Column(db.Date, nullable=False)
    occupation = db.Column(db.String(120), nullable=False)




@app.route('/', methods=['GET, POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        date = request.form['date']
        date_format = datetime.strptime(date, '%d-%m-%Y')
        occupation = request.form['occupation']

        form = Form(first_name=first_name, last_name=last_name,
                    email=email, phone=phone, date=date,
                    occupation=occupation)
        db.session.add(form)
        db.session.commit()

        message = Message(subject="Job Application",
                          sender=app.config.get("MAIL_USERNAME"),
                          recipients=[email],
                          body=f"Dear {first_name},\n\nThank you for applying for the job.\n\n here is your data:\n\nFirst Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nOccupation: {occupation}\n\nBest Regards,\n\n{app.config.get('MAIL_USERNAME')}. \n\n We will contact you soon.")

        flash(f"{first_name},Form submitted successfully", "success")

    return render_template('templates/index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
