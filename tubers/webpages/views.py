from django.shortcuts import redirect, render
from .models import Slider, Team, Contact, About
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
    teams = Team.objects.all()
    about = About.objects.all()

    data = {
        'teams': teams,
        'about': about
    }

    return render(request, 'webpages/about.html', data)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']

        contacts = Contact(name=name, phone=phone, email=email, company=company, subject=subject, message=message)
        contacts.save()
        return redirect('home')

    return render(request, 'webpages/contact.html')


def services(request):
    return render(request, 'webpages/services.html')

