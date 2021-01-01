from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django.utils import timezone






class Message(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=70)
	subject=models.CharField(max_length=100)
	message=models.CharField(max_length=300)


	def __str__(self):
		return self.name


class Job(models.Model):
	companyname=models.CharField(max_length=100,blank=True)
	slug=models.SlugField(max_length=300,unique=True)
	postname=models.TextField(blank=True)
	vac=models.IntegerField(blank=True)
	qualifiction=models.CharField(max_length=50,blank=True)
	lastdate=models.DateTimeField(editable=True)

	jobcat=models.CharField(max_length=100,blank=True)
	jobloc=models.CharField(max_length=100,blank=True)
	jobdes=models.TextField(blank=True)
	salary=models.TextField(blank=True)
	eligibility=models.TextField(blank=True)
	agelimit=models.CharField(max_length=100,blank=True)
	appfee=models.TextField(blank=True)
	impdate=models.TextField(blank=True)
	applyproc=models.TextField(blank=True)
	postedon=models.DateTimeField(auto_now_add=True)
	link=models.URLField(blank=True)




	class Meta:
		ordering=['-postedon']


	def __str__(self):
		return self.postname







