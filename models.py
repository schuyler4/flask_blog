import datetime
from sqlalchemy import String, Column, Integer, create_engine, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import func


Base = declarative_base()
engine = create_engine('sqlite:///data.db', echo=True)
Session = sessionmaker(bind=engine)
db_session = Session()


class Blog_Post(Base):
	id = Column ('blog_post_id', Integer, primary_key=True)
	date_created = Column(DateTime(timezone=True), server_default=func.now())
	date_updated = Column(DateTime(timezone=True), onupdate=func.new())
	title = Column(String)
	sub_title = Column(String)
	content = Column(String)
	comments = relationship("Comments", backref="Blog_Post")
	__tablename__ = "Blog_Post"

	def __init__(self, title, sub_title, content):
		self.title = title
		self.sub_title = sub_title
		self.content = content


class Comments(Base):
	blog_post_id = Column(Integer, ForeignKey(Blog_Post.id),primary_key=True)
	name = Column(String(50))
	content = Column(String(150))
	blog_post = relationship('Blog_Post', cascade="all,delete",backref="Comments")
	__tablename__ = "Comments"

	def __init__(self, name, content, blog_post):
		self.name = name
		self.content = content
		self.blog_post = blog_post

class Email_User(Base):
	id = Column('blog_post_id', Integer, primary_key=True)
	first_name = Column(String)
	last_name = Column(String)
	email_address = Column(String)
	__tablename__ = "Email_User"

	def __init__(self, first_name, last_name, email_address):
		self.first_name = first_name
		self.last_name = last_name
		self.email_address = email_address

Base.metadata.create_all(engine)

	
	
