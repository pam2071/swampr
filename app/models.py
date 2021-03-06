#class Post:
#		def __init__(self, title, author, content): #The initialization method
#			self.title = title                      #Defining the title attribute
#			self.author = author                    #Defining the author attribute
#			self.content = content                  #Defining the content attribute

from app import db


class User(db.Model):
	id = (db.Column(db.Integer,primary_key = True))
	firstname = db.Column(db.String(64))
	lastname = db.Column(db.String(64))
	username = db.Column(db.String(120), unique =True)
	posts = db.relationship('Post', backref = 'author')

def enabled_categories():
    return Category.query.filter_by(enabled = True)

class BlogPost(db.Model):
  id = (db.Column(db.Integer,primary_key = True))
  title    = db.Column(db.String(50))
  blog     = db.Column(db.String(250))
# category = db.Column(db.QuerySelectField(query_factory = enabled_categories, allow_blank = True))

def edit_blog_post(request, id):
    post = Post.query.get(id)
    form = BlogPostEdit(obj = post)
   # Since we didn't provide a query_factory for the 'blog' field, we need
   # to set a dynamic one in the view.
    form.blog.query = Blog.query.filter(Blog.author == request.user).order_by(Blog.name)

		
