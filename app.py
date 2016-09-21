from flask import Flask
from flask_mail import Mail, Message
#from route import sendMail

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "%^RTYJH(*UUY&TYGTR%^HG"
mail = Mail(app)
#MAIL_SERVER = 'marek.s.newton@gmail.com'
#MAIL_POST = 25
#MAIL_USERNAME = None
#MAIL_PASSWORD = None
#ADMINS = ['marek.s.newton@gmail.com']

#sendMail(mail)

from route import routes
app.register_blueprint(routes)


if(__name__ == "__main__"):
	app.run()
