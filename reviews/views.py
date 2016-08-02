# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Reviews_Form
from thanks.forms import QuestionForm
from .models import Reviews
from django.utils.translation import ugettext as _
import datetime
# Create your views here.

def reviews(request):
	errors = []
	question_form = QuestionForm()
	message = "Thanks"
	review_info = _(u"You can write your comments about us. Evaluate our work. We will be very grateful")
	if request.method=='POST':
		# create a form instance and populate it with data from the request:
		form = Reviews_Form(request.POST)
		#check whether it's valid:
		if form.is_valid():
			# set a reviews:
			rev = Reviews(sender_name=form.cleaned_data['sender_name'], 
						  message=form.cleaned_data['message'], 
						  pub_date = datetime.datetime.now() + datetime.timedelta(hours=3))
			rev.save()
			reviews_db = Reviews.objects.filter().order_by('-pub_date')
			return render(request, 'reviews/reviews.html', {'form': form, 
															'errors': errors, 
															'all_reviews': reviews_db, 
															'question_form': question_form, 
															'message': message,
														    'review_info': review_info})
		else:
			if not request.POST.get('sender_name', ''):
				errors.append(_(u"Enter a sender name"))
			if not request.POST.get('message', ''):
				errors.append(_(u"Enter a message"))
			reviews_db = Reviews.objects.filter().order_by('-pub_date')
			return render(request, 'reviews/reviews.html', {'form': form, 
															'errors': errors, 
															'all_reviews': reviews_db, 
															'question_form': question_form,
														    'review_info': review_info})
	else:
		form = Reviews_Form()
		reviews_db = Reviews.objects.filter().order_by('-pub_date')
	return render(request, 'reviews/reviews.html', {'form': form, 
													'errors': errors, 
													'all_reviews': reviews_db, 
													'question_form': question_form,
												    'review_info': review_info})