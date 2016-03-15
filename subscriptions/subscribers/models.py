from __future__ import unicode_literals

from django.db import models
from localflavor.us.models import USStateField, USZipCodeField
from django.contrib.auth.models import User

class Subscriber(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	end_date = DateTimeField('End Date')
	PRINT = 'P'
	EMAIL = 'E'
	BOTH = 'B'
	SUBSCRIPTION_TYPE = (
		(PRINT, 'Print'),
		(EMAIL, 'Email'),
		(BOTH, 'Both')
		)
	subscription_type = models.CharField(max_length=1, 
		choices=SUBSCRIPTION_TYPE, default=PRINT)
	line1 = models.CharField(max_length=200)
	line2 = models.CharField(max_length=200)
	state = USStateField()
	zip_code = USZipCodeField()

class Package(models.Model):
	name = models.CharField(max_length=500)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	months = models.IntegerField()

class Transaction(models.Model)
	subscriber = models.ForeignKey(Subscriber)
	date = DateTimeField('Transaction Date')
	paid = models.DecimalField(max_digits=5, decimal_places=2)
	received = models.CharField(max_length=200)
	notes = models.CharField(max_length=200)