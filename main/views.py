from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message

@login_required
def chat_view(request):
    messages = Message.objects.all()
    form = MessageForm(request.POST or None)
    if form.is_valid():
        message = form.save(commit=False)
        message.owner = request.user
        message.save()
        return redirect('chat')

    return render(request, 'chat.html', {'messages': messages, 'form': form})

