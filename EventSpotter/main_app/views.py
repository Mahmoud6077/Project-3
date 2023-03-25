from django.shortcuts import render, redirect
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Events, Ticket
from .forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

##

# Define the home view
def home(request):
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    events = Events.objects.all()
    # return render(request, 'home.html')

    # Pagination
    paginator = Paginator(events, 1) # 1 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'events':events} )

def about(request):
    # return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    return render(request, 'about.html')

@login_required
def events_index(request):
    events = Events.objects.all()
    page_number=2
    paginator = Paginator(events, page_number) # 1 posts per page
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, show the first page
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), show the last page of results
        items = paginator.page(paginator.num_pages)

    return render(request, 'events/index.html', {'events':events, 'page':items} )

@login_required
def events_detail(request, event_id):
    event = Events.objects.get(id= event_id) 
    return render(request, 'events/detail.html', {'event': event})

@login_required
def events(request):
    return render(request, 'events/Events.html')

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

@login_required
def profile(request):
    return render(request, 'profile.html')


class EventCreate(LoginRequiredMixin, CreateView):
    model = Events
    fields = ['name', 'location', 'description', 'date', 'time', 'image']   
    # success_url = '/home'
    def form_valid(self, form):
        # self.request.user is the logged user
        form.instance.user = self.request.user
        # Allows CreateView form_valid method to do its normal work
        return super().form_valid(form)
    
class EventUpdate(LoginRequiredMixin,UpdateView):
    model = Events
    fields = ['location', 'date', 'time','description']


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Events
    success_url = '/events/'

@login_required
def EventBooking(request,event_id):
    event = Events.objects.get(id=event_id)
    # user_id = User.objects.get(user_id = request.user)
    # if request.method == 'POST':
    #     ticket_count = int(request.POST['ticket_count'])
        
    #     for i in range(ticket_count):
    #         ticket = Ticket.objects.create(
    #             event=event,
    #             ticket_number=20,
    #         )
    return render(request, 'events/booking.html', {'events':event})


@login_required
def ticket_history(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'profile.html', {'tickets': tickets})
    # return render(request, 'ticket_history.html', {'tickets': tickets})

@login_required
def booking_success(request, event_id):
    event = Events.objects.get(id=event_id)
    context = {'event': event, 'event_id': event_id}
    return render(request, 'events/booking_success.html', context)