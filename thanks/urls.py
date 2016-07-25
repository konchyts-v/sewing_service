from django.conf.urls import url
from . import views

app_name = 'thanks'
urlpatterns = [
	url(r'^question/$', views.thanks_for_question, name='thanks_for_question'),
]