from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    f_yt = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    yt = Youtuber.objects.order_by('-created_date')

    data = {
        'sliders': sliders,
        'teams': teams,
        'f_yt': f_yt,
        'yt': yt
    }

    return render(request, 'webpages/home.html', data)


def about(request):
    return render(request, 'webpages/about.html')


def contact(request):
    return render(request, 'webpages/contact.html')


def services(request):
    return render(request, 'webpages/services.html')

