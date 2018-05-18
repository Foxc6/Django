# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def RegVal(self, PostData):
		results = {'status': True, 'errors': []}
		if len(PostData['name']) < 2:
			results['errors'].append('Your first name must be greater than 1 character.')
		# Add check to see if user is in db


		if len(results['errors']) > 0:
			results['status'] = False
		return results

	def UserCreator(self, PostData):
		user = User.objects.create(
			name = PostData['name'], 
			age = PostData['age'], 
			)
		return user

	def CommentCreator(self, PostData):
		comment = Comment.objects.create(
			content = PostData['content'], 
			user_id = request.session['user_id'], 
			)
		return comment

	def check_age(request):
		user_age = request.session['user_age']
		user_id = request.session['user_id']
		print user_age
		print user_id
		return user_age
	
	def LogVal(self, PostData):
		results = {'status': True, 'errors': [], 'user': None}
		users = self.filter(name = PostData['name'])
		if len(users) < 1:
			results['errors'].append('User not found')
		if len(results['errors']) > 0:
			results['status'] = False
		else: 
			results['user'] = users[0]
		return results

class User(models.Model):
	name = models.CharField(max_length=255)
	age = models.IntegerField()
	objects = UserManager()

class Comment(models.Model):
	content = models.TextField(max_length=255)
	user = models.ForeignKey(User, related_name = "comments")
	objects = UserManager()