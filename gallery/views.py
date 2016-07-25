from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from thanks.forms import QuestionForm
from .models import Photo
from thanks import messages
from django.utils.translation import ugettext as _

# Create your views here.

def gallery(request):
	review_info = _(u"Please visit our photo gallery. Here are pictures of the process, and other areas.")
	errors = []
	question_form = QuestionForm()
	photos = Photo.objects.all()
	if(photos):
		return render(request, 'gallery/gallery.html', 
				  	{'errors': errors, 
					 'question_form': question_form, 
					 'photos': photos,
					 'review_info': review_info})
	else:
		return render(request, 'thanks/information_page.html', 
					  {'message': messages.message_404, 
					   'title': messages.title_404, 
					   'question_form': question_form})
	