from django.shortcuts import render
from django.utils import timezone
from .models import Challenge
from django.template.loader import get_template

# Create your views here.

def landing(request):
    return render(request, 'challenges/landing.html',{'landing': landing})

def active_challenge(request):
    active_challenge = Challenge.objects.filter(challenge_active=True)
    return render(request, 'challenges/active_challenge.html',
    {'active_challenge': active_challenge})

def old_challenges(request):
    old_challenge = Challenge.objects.filter(challenge_start__lte=timezone.now(), challenge_active=False)
    return render(request, 'challenges/old_challenges.html', {'old_challenge' : old_challenge})
    #
    # old_challenges = Challenge.objects.filter(
    # challenge_stop__lte=timezone.now()).order_by('challenge_start')
    # return render(request, 'challenges/landing.html',
    # {'old_challenges': old_challenges})
