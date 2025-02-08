from django.shortcuts import render, redirect

from Events.forms import AddForm
from Events.models import Event


# Create your views here.

def index(request):
    events = Event.objects.filter(user=request.user)
    return render(request, "index.html", {"events": events})


def add(request):
    # form = AddForm()
    if request.method == "POST":
        form_data = AddForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            event = form_data.save(commit=False)
            event.user = request.user
            event.poster = form_data.cleaned_data['poster']
            event.save()
            return redirect("index")
    return render(request, "add.html",{"form":AddForm})
