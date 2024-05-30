from django.shortcuts import render
from django.http import HttpResponse
from .chatbot import handle_user_input

# Create your views here.
def index(request):
    return render(request,'index.html')

def sendAnswer(request):
    msg = request.GET.get('msg')
    return HttpResponse(handle_user_input(msg))
