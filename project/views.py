#! coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.edit import CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from project.models import *
import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
import settings


def participant_name(request, event_pk, pk):
    participant = Participant.objects.get(pk=pk)
    return HttpResponse(participant.username)

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

    def form_valid(self, form):
        participant = form.save()
        participant.event_set.add(self.kwargs['event_pk'])
        participant.save()
        return super(ParticipantCreate, self).form_valid(form)

class ParticipantDelete(DeleteView):
    model = Participant
    success_url = reverse_lazy('event-list')


class Certificate(View):
    def get(self, request, *args, **kwargs):
        context_dict = {
            'event': Event.objects.get(pk=kwargs['event_pk']),
            'participant': Participant.objects.get(pk=kwargs['pk']),
        }

        template = get_template('project/certificate.html')
        context = Context(context_dict)
        context.update({
            'FONTS_DIR': settings.FONTS_DIR,
        })

        html  = template.render(context)

        input_ = StringIO.StringIO(html.encode("UTF-8"))
        file_ = StringIO.StringIO()
        pdf = pisa.pisaDocument(input_, file_)

        if not pdf.err:
            return HttpResponse(file_.getvalue(), mimetype='application/pdf')
        return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


