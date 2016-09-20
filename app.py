from flask import Flask
#from flask_mail import Mail, Message

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "%^RTYJH(*UUY&TYGTR%^HG"
#mail = Mail(app)


from route import routes
app.register_blueprint(routes)


if(__name__ == "__main__"):
	app.run()
