from flask import Blueprint, render_template, request, session, redirect, url_for, flash, session
from models import Blog_Post, Comments, db_session, Email_User
from sqlalchemy import *
from sqlalchemy.orm import *
routes = Blueprint('routes', __name__)


admin_username = "admin"
admin_password = "admin"


@routes.route("/")
def home():
	return render_template('home.html')

@routes.route("/admin", methods=["GET", "POST"])
def check_admin():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if(username == admin_username and password == admin_password):
			return redirect(url_for('routes.add_blog'))
			session["logged_in"] = True
		else:
			flash("are you sure your an admin something was not entered correctly")
			return redirect(url_for('routes.check_admin'))
	return render_template("admin.html")


@routes.route("/addblogpost", methods=["GET", "POST"])
def add_blog():

	if request.method == 'POST':
		title = request.form['title']
		sub_title = request.form['subtitle']
		content = request.form['content']
		new_blog_post = Blog_Post(title, sub_title, content)
		print "panda"
		print new_blog_post
		print "gallop"
		db_session.add(new_blog_post)
		try:
			db_session.commit()
		except exc.SQLAlchemyError:
			print "error"
			pass
		return redirect(url_for('routes.blog_post', blog_post_title=title))
	if(session["logged_in"] == True):
		return render_template("addpost.html")
	else:
		return redirect(url_for('routes.check_admin'))


@routes.route("/addemaillist", methods=['GET', 'POST'])
def add_email_list():
	if request.method == 'POST'
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		email_address = request.form['email_address']
		new_email_user = Email_User(first_name, last_name, email_address)
		db_session.add(new_email_user)
		try:
			db_session.commit()
		except exc.SQLAlchemyError:
			print "error"
			pass
		return redirect(url_for('routes.add_blog'))
	if(session['logged_in'] == True):
		return render_template("")

@routes.route("/blogpost/<blog_post_title>", methods=["GET", "POST"])
def blog_post(blog_post_title):
	whole_blog_post = db_session.query(Blog_Post).filter(Blog_Post.title == blog_post_title).first()
	blog_post_comments = db_session.query(Blog_Post).options(lazyload('comments')).all()
	if request.method == 'POST':
		user_name = request.form['user_name']
		content = request.form['content']
		new_comment = Comments(user_name, content, whole_blog_post)
		db_session.add(new_comment)
		try:
			db_session.commit()
		except exc.SQLAlchemyError:
			print "error"
			pass
		return redirect(url_for('routes.blog_post',blog_post_title=whole_blog_post.title))
	return render_template('blogpost.html', blog_post = whole_blog_post, comments = blog_post_comments)


@routes.route("/listblogpost")
def list_blog_post():
	all_blog_posts = db_session.query(Blog_Post).all()
	print all_blog_posts
	return render_template("listblogposts.html", blog_posts = all_blog_posts)


@routes.errorhandler(404)
def not_found_error(error):
	return render_template('404.html') ,404

