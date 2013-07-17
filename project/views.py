#! coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from project.models import Event, Participant


def index(request):
    return HttpResponseRedirect('/events/') # render_to_response('index.html', {})

class EventList(ListView):
    model = Event

class EventCreate(CreateView):
    model = Event

class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('event-list')

class ParticipantCreate(CreateView):
    model = Participant
