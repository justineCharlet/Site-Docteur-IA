from django.http import HttpResponse
from django.shortcuts import render
from presentation.models import Education

def home(request):
    return HttpResponse('<h1>Home</h1>')

def aboutme(request):
    education = Education.objects.all()
    return render(request, 'presentation/aboutme.html')




