from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
	url(r'^$', views.main_func, name = "Main_Func"),
]