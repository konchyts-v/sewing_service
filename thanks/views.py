# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import QuestionForm
from django.core.mail import send_mail, BadHeaderError
from thanks import messages
from django.utils.translation import ugettext as _

# Create your views here.

def thanks_for_question(request):
	errors=[]
	question_form = QuestionForm()
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = QuestionForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			subject = form.cleaned_data['title']
			message = form.cleaned_data['body']
			sender = form.cleaned_data['sender']
			if subject and message and sender:
				try:
					recipients = ['vitaliy.konchyts@gmail.com']
					send_mail(subject, message, sender, recipients)
				except BadHeaderError:
					return render(request, 'thanks/information_page.html', {'message': messages.message_error, 'title': messages.title_error, 'question_form': question_form})
				return render(request, 'thanks/information_page.html', {'message': messages.message_correct, 'title': messages.title_correct, 'question_form': question_form})
		else:
			if not request.POST.get('subject', ''):
				errors.append(_(u"Please, enter the subject."))
			if not request.POST.get('message', ''):
				errors.append(_(u"Please, enter the message."))
			if not request.POST.get('sender', ''):
				errors.append(_(u"Please, enter the sender name"))
			return render(request, 'thanks/information_page.html', {'title': messages.title_error, 'message': messages.message_error, 'question_form': question_form})
	
	return render(request, 'thanks/information_page.html', {'title': messages.title_404, 'message': messages.message_404, 'question_form': question_form})

# function 404 Not Found
def Not_Found(request):
	question_form = QuestionForm()
	return render(request, 'thanks/information_page.html', {'title': messages.title_404, 'message': messages.message_404, 'question_form': question_form})