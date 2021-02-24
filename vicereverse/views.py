from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    user_text = request.GET['user_text']
    reversed_text = user_text[::-1]
    length_text = len(user_text.split())
    return render(request, 'home.html', {'userText': user_text, 'reversedText': reversed_text, 'lengthText': length_text})
