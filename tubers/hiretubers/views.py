from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Hiretuber

def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_name = request.POST['tuber_name']
        tuber_id = request.POST['tuber_id']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
	
        hiretubers = Hiretuber(first_name=first_name, last_name=last_name, tuber_name=tuber_name, tuber_id=tuber_id, city=city, phone=phone, state=state, email=email, message=message, user_id=user_id)
        hiretubers.save()
        messages.success(request, 'thanks for reaching out...')
        return redirect('youtubers')

