from django.shortcuts import render
from . models import Message
from .forms import MessageForm

# Create your views here.

def index(request):
    obj = Message.objects.all()
    form = MessageForm()
    if request.method =='POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            form = MessageForm()
    
    return render(request, 'index.html',{'form':form, 'obj':obj})