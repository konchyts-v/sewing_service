from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import About
from thanks.forms import QuestionForm
from django.utils.translation import ugettext as _

# Create your views here.

def aboutus(request):
	about_info = get_object_or_404(About)
	question_form = QuestionForm()
	return render(request, 'aboutus/about.html',
				 {'general_information': about_info.general_information,
				  'first_location': about_info.first_location,
				  'second_location': about_info.second_location,
				  'first_phone': about_info.first_phone,
				  'second_phone': about_info.second_phone,
				  'schedule_first': about_info.schedule_first,
				  'schedule_second': about_info.schedule_second,
				  'advantages': about_info.advantages,
				  'question_form': question_form})