#import django function url:
from django.conf.urls import url
#import all views from challenges application:
from . import views


#assign a view called challenges_list to ^$ URL (only empty string will match) > 'http://127.0.0.1:8000/' is not a part of the URL
urlpatterns = [
    url(r'^$',views.landing, name='landing'),
    url(r'^$',views.challenges_list, name='challenges_list'),
    url(r'^$',views.old_challenges, name='old_challenges'),
]
