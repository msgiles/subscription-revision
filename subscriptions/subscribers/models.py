from __future__ import unicode_literals

from django.db import models

class Subscriber(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	email = models.EmailField(max_length=254)
	# TODO: Address 
	end_date = DateTimeField('End Date')
	history = models.ManyToManyField('Transaction')

class Package(models.Model):
	name = models.CharField(max_length=500)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	months = models.IntegerField()

class Transaction(models.Model)
	date = DateTimeField('Transaction Date')
	paid = models.DecimalField(max_digits=5, decimal_places=2)
	received = models.CharField(max_length=200)
	notes = models.CharField(max_length=200)