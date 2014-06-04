
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class NewUserForm(Form):
	firstname = TextField('firstname')
	lastname = TextField('lastname')
	username = TextField('username', validators = [Required()])



	
