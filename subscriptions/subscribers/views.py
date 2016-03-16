from django.shortcuts import render
from django.template import loader

from django.contrib.auth.models import User
from .models import Subscriber

def list(request):
	subscribers_list = Subscriber.objects.all
	template = loader.get_template('subscribers/list.html')
	context = {
		'subscribers_list' : subscribers_list,
	}
	return render(request, 'subscribers/list.html', context)