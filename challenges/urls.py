#import django function url:
from django.conf.urls import url
#import all views from challenges application:
from . import views


#assign a view called landing to ^$ URL (only empty string will match) > 'http://127.0.0.1:8000/' is not a part of the URL
urlpatterns = [
    url(r'^$',views.landing, name='landing'),
    url(r'^$',views.active_challenge, name='active_challenge'),
    url(r'^$',views.old_challenges, name='old_challenges'),
]
