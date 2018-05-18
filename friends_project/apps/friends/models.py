from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
	def RegistrationValidator(self, PostData):
		results = {'status': True, 'errors': []}
		if len(PostData['name']) < 2:
			results['errors'].append('Please enter a name that is longer than 1 character!')
		if len(PostData['alias']) < 2:
			results['errors'].append('Please enter an alias that is greater than 1 character!')
		if not re.match('(\w+[.|\w])*@(\w+[.])*\w+', PostData['email']):
			results['errors'].append('Invalid email, please try again!')
		if len(PostData['password']) < 8:
			results['errors'].append('Invalid password, please enter a password that is greater than 8 characters!')
		if PostData['password'] != PostData['c_password']:
			results['errors'].append('Passwords do not match!')
		# Add check to see if user is in db
		if len(self.filter(email = PostData['email'])) > 0:
			results['errors'].append('Account already exists. You may login to continue!')

		if len(results['errors']) > 0:
			results['status'] = False
		return results
	
	def UserCreator(self, PostData):
		hashed = bcrypt.hashpw(PostData['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(
			name = PostData['name'], 
			alias = PostData['alias'], 
			email = PostData['email'],
			birthday = PostData['birthday'], 
			password = hashed
			)
		return user
	
	def LoginValidator(self, PostData):
		results = {'status': True, 'errors': [], 'user': None}
		users = self.filter(email = PostData['email'])
		if len(users) < 1:
			results['errors'].append('User not found')
		else:
			if bcrypt.checkpw(PostData['password'].encode(), users[0].password.encode()) == False:
				results['errors'].append('Invalid password')
		if len(results['errors']) > 0:
			results['status'] = False
		else: 
			results['user'] = users[0]
		return results


class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	birthday = models.DateField(blank=False, null=True)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	friends = models.ManyToManyField("self", related_name = "friend")
	objects = UserManager()