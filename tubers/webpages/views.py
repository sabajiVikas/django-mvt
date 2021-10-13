from django.shortcuts import render
from .models import Slider, Team


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()


    data = {
        'sliders': sliders,
        'teams': teams
    }

    return render(request, 'webpages/home.html', data)


def about(request):
    return render(request, 'webpages/about.html')


def contact(request):
    return render(request, 'webpages/contact.html')


def services(request):
    return render(request, 'webpages/services.html')

