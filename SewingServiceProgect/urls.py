"""SewingServiceProgect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from thanks import views
from main.views import main_func
from django.conf import settings
from django.conf.urls.static import static
from .settings import MEDIA_ROOT, DEBUG
from django.views.static import serve
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^aboutus/', include('aboutus.urls')),
	url(r'^order/', include('order.urls')),
	url(r'^gallery/', include('gallery.urls')),
	url(r'^reviews/', include('reviews.urls')),
	url(r'^thanks/', include('thanks.urls')),
	url(r'^', include('main.urls')),
	
	
	#url(r'^', views.Not_Found, name = 'Not_Found'),
]

#if DEBUG:
#	urlpatterns += ['',
#		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#			'document_root': MEDIA_ROOT})]
if DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': MEDIA_ROOT,
        }),
    ]
	
urlpatterns += [
	url(r'^', views.Not_Found, name = 'Not_Found'),
	]