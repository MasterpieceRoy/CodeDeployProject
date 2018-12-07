from django.shortcuts import render
from .models import Games
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
# games = [
#     {
#         'developer': 'Activision',
#         'name': 'Call Of Duty',
#         'release': '2018',
#         'creator': 'Activision',
#     },
#     {
#         'developer': 'Blizzard',
#         'name': 'Overwatch',
#         'release': '2008',
#         'creator': 'Jeff Kaplan',
#     }
# ]


def home(request):
    context = {
        'games': Games.objects.all()
    }
    return render(request, 'web/home.html', context)


@login_required
def about(request):
    return render(request, 'web/about.html', {'title': 'About'})


