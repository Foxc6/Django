from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
	def RegVal(self, PostData):
		results = {'status': True, 'errors': []}
		if len(PostData['name']) < 2:
			results['errors'].append('Your first name must be greater than 1 character.')
		if len(PostData['alias']) < 2:
			results['errors'].append('Your last name must be greater than 1 character.')
		if not re.match('(\w+[.|\w])*@(\w+[.])*\w+', PostData['email']):
			results['errors'].append('Please enter a valid email')
		if len(PostData['password']) < 5:
			results['errors'].append('Your password must be greater than 5 characters')
		if PostData['password'] != PostData['c_password']:
			results['errors'].append('Your password does not match!')
		# Add check to see if user is in db
		if len(self.filter(email = PostData['email'])) > 0:
			results['errors'].append('An account for this user already exists! Please login.')

		if len(results['errors']) > 0:
			results['status'] = False
		return results
	
	def creator(self, PostData):
		hashed = bcrypt.hashpw(PostData['password'].encode(), bcrypt.gensalt())
		user = User.objects.create(
			name = PostData['name'], 
			alias = PostData['alias'], 
			email = PostData['email'],
			birthday = PostData['birthday'], 
			password = hashed
			)
		return user
	
	def LogVal(self, PostData):
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
	poked_users = models.ManyToManyField("self", related_name = "poked_by", symmetrical=False)
	objects = UserManager()

