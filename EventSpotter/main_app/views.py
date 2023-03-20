from django.shortcuts import render, redirect
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Events
from .forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

##
# Define the home view
def home(request):
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    events = Events.objects.all()
    return render(request, 'home.html', {'events':events} )
    # return render(request, 'home.html')

def about(request):
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    return render(request, 'about.html')

def events_index(request):
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    events = Events.objects.all()
    return render(request, 'events/index.html', {'events':events} )

def events_detail(request, event_id):
    event = Events.objects.get(id= event_id) 
    return render(request, 'events/detail.html', {'event': event})

def signup(request):
    error_message =''
    if request.method == 'POST':
        #Make a 'User' form object with the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save user to DB
            user = form.save()
            #login the user automaticlly once they signed up 
            login(request, user)
            return redirect('home')
        
        else:
            error_message = 'Invalid: Please Try Again'
    #if there is a bad post or a get request
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)


def profile(request):
    return render(request, 'profile.html')