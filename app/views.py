# -*- coding: utf-8 -*- 

from app import app
from flask import render_template
from models import Post


@app.route('/')
def index():
	some_post = Post("Not much to say", "Aliya", "Today was an uneventful day")
	some_other_post = Post("I had an Aha Moment", "Pam",  "It made me misty I guess I saw the light")
	seventh_week_post = Post("Extra Amazing Week", "Pam", "Went to AFLCIO to see Nicole my Mentor AND a Rooftop Party at Perrys")
	seventh_week_day4_post = Post("TGIAF", "Pam", "And this week is not even close to being over Transparency Camp on Saturday")
	
	return render_template ("index.html", posts = [some_post, some_other_post, seventh_week_post, seventh_week_day4_post])







	
