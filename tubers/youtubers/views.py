from django.shortcuts import render


def youtubers(request):
    return render(request, 'youtubers/youtubers.html')


def youtuber_detail(request, id):
    return render(request, 'youtubers/youtuber_detail.html')


def search(request):
    return render(request, 'youtubers/search.html')
