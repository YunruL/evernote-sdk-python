"""evernote_oauth_sample URL Configuration

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
from django.conf.urls import url
from oauth import views

app_name = 'oauth'

urlpatterns = [
	url(r"^oauth/$", views.index, name = "evernote_index"),
	url(r"^oauth/auth/$", views.auth, name = "evernote_auth"),
	url(r"^oauth/callback/$", views.callback, name = "evernote_callback"),
	url(r"^oauth/reset/$", views.reset, name="evernote_auth_reset"),
]
	
    