from django.conf.urls import url
from . import views

app_name = 'order'
urlpatterns = [
	url(r'^$', views.send_order, name='send_order'),
]