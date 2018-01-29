"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^challenges/', include('challenges.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

#import challenges.urls to keep mysite/urls.py clean:
#django will direct everything that comes into 'http://127.0.0.1:8000/' to challenges.urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('challenges.urls')),
]
