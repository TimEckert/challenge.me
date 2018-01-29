from django.shortcuts import render

# Create your views here.
def challenges_list(request):
    return render(request, 'challenges/challenges_list.html',{})
