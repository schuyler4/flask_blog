from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "%^RTYJH(*UUY&TYGTR%^HG"


from route import routes
app.register_blueprint(routes)


if(__name__ == "__main__"):
	app.run()
