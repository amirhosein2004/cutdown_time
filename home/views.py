from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Event  
from .forms import createEventform, EditEventform


def home(request):
    all_events = Event.objects.all()
    return render(request, 'list_events.html', {'all_events':all_events})


def countdown_timer(request, pk_event):
    try:
        event = Event.objects.get(pk=pk_event)  # Retrieve the Event object
        if event:
            time_remaining = event.event_date - timezone.now()  # Calculate time remaining
            hours = time_remaining.seconds // 3600
            minutes = (time_remaining.seconds % 3600) // 60
            seconds = time_remaining.seconds % 60
            data = {
                'id': event.pk,
                'name': event.name,
                'hours': hours,
                'minutes': minutes,
                'seconds': seconds
        }
    except:
        return HttpResponse('Object Does Not Exists.')
    
    return render(request, 'detail_event.html', {'data': data})


def create_event(request):
    form = createEventform()

    if request.method == 'POST':
        form = createEventform(request.POST)
        if form.is_valid():

            event = Event.objects.create(
                name=form.cleaned_data['name'], 
                event_date=form.cleaned_data['event_date']
            )

            return redirect('countdown_timer', event.id)
        
    return render(request, 'create_event.html', {'form':form})


def edit_event(request, pk_event):
    event = Event.objects.get(pk=pk_event)
    form = EditEventform()

    if request.method == 'POST':
        form = createEventform(request.POST, instance=event)
        if form.is_valid(): 
            event = form.save(commit=False)
            event.name = form.cleaned_data['name']
            event.event_date = form.cleaned_data['event_date']
            event.save()
            return redirect('home')

    return render(request, 'edit_event.html', {'form':form})


def remove_event(request, pk_event):
    Event.objects.get(pk=pk_event).delete()
    return redirect('home')
