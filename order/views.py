from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from thanks.forms import QuestionForm
from thanks import messages
from django.utils.translation import ugettext as _

# Create your views here.

def send_order(request):
	errors = []
	review_info = _(u"To use our services, you only need to order from the comfort of your home.\
					Will execute your order correctly. Determine what services you want available.\
					We will contact you via e-mail, and say what day and where you will be better to come. Thank you.")
	question_form = QuestionForm()
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			if subject and message and sender:
				try:
					recipients = ['vitaliy.konchyts@gmail.com']
					send_mail(subject, message, sender, recipients)
				except BadHeaderError:
					return render(request, 'thanks/information_page.html',
								  {'message': _(messages.message_error), 
								   'title': _(messages.title_error), 
								   'question_form': question_form})
				return render(request, 'thanks/information_page.html', 
							  {'message': messages.message_correct, 
							   'title': messages.title_correct, 
							   'question_form': question_form})
		else:
			if not request.POST.get('subject', ''):
				errors.append(_("Please, enter the subject."))
			if not request.POST.get('message', ''):
				errors.append(_("Please, enter the message."))
			if not request.POST.get('sender', ''):
				errors.append(_("Please, enter the sender name"))
			return render(request, 'order/order.html', 
						  {'form': form, 
						   'errors': errors, 
						   'question_form': question_form,
						   'review_info': review_info})
	else:
			form = ContactForm()
	return render(request, 'order/order.html', 
				  {'form': form, 
				   'question_form': question_form,
				   'review_info': review_info})