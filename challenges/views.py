from django.shortcuts import render
from django.utils import timezone
from .models import Challenge
from django.template.loader import get_template

# Create your views here.

# def challenges(request):
#     active_challenges = Challenge.objects.filter(challenge_active=True)
#     old_challenges = Challenge.objects.filter(challenge_start__lte=timezone.now(), challenge_active=False)
#     return render(request, 'challenges/landing.html', {'challenges': challenges})

def challenges(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/landing.html', {'challenges' : challenges})
    some_challenges = Challenge.objects.filter(title__contains='Console')
    return render(request, 'challenges/landing.html', {'some_challenges' : some_challenges})
