from django.shortcuts import render
from django.utils import timezone
from .models import Challenge

# Create your views here.
def challenges_list(request):
    challenges = Challenge.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'challenges/challenges_list.html',{'challenges': challenges})
