from django.shortcuts import render
from django.utils import timezone
from .models import Challenge
from django.template.loader import get_template

# Create your views here.
def landing(request):
    return render(request, 'challenges/landing.html', {'landing': landing})

def challenges_list(request):
    challenges = Challenge.objects.filter(challenge_start__lte=timezone.now())
    return render(request, 'challenges/challenges_list.html',
    {'challenges': challenges})

def old_challenges(request):
    return render(request, 'challenges/old_challenges.html', {})
    #
    # old_challenges = Challenge.objects.filter(
    # challenge_stop__lte=timezone.now()).order_by('challenge_start')
    # return render(request, 'challenges/challenges_list.html',
    # {'old_challenges': old_challenges})
