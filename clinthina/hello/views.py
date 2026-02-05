from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    return render(request, 'hello/home.html')

def services(request):
    return render(request, 'hello/services.html')

def faq(request):
    return render(request, 'hello/faq.html')

def contact(request):
    return render(request, 'hello/contact.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'hello/signup.html', {'form': form})