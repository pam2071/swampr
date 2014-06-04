# -*- coding: utf-8 -*- 

from app import app, db                    #Import our app components from other files
from flask import Flask, render_template, redirect
from models import Post, User
from forms import NewUserForm



@app.route('/')
def index():                                #This is the landing page
	all_users= User.query.all()
        posts = Post.query.all()
	return render_template("index.html", users = all_users, posts = posts)

	
@app.route('/add_user', methods = ['GET', 'POST'])
def add_user():
	form = NewUserForm()
	if form.validate_on_submit():
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		return redirect('/')
	return render_template("add_user.html", form = form)

def add_post():
	form = BlogPostForm()
	if form.validate_on_submit():
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		return redirect('/')
	return render_template("add_user.html", form = form)	




	
