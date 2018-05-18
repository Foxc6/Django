# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import datetime, date

class UserManager(models.Manager):
	def RegVal(self, PostData):
		results = {'status': True, 'errors': []}
		if len(PostData['first_name']) < 2:
			results['errors'].append('Your first name must be greater than 1 character.')
		if len(PostData['last_name']) < 2:
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
			first_name = PostData['first_name'], 
			last_name = PostData['last_name'],
			birthday = PostData['birthday'], 
			email = PostData['email'], 
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

	def calculate_age(birthday):
		today = date.today()
		return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	birthday = models.DateField(blank=False, null=True)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()