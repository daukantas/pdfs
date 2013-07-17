from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _


class Participant(models.Model):
    username = models.CharField(max_length=255)
    topic = models.TextField()

    def get_absolute_url(self):
        return reverse('event-list')


class Event(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    moto = models.CharField(_('Moto'), max_length=255)
    logo = models.ImageField(_('Logo'), upload_to='media/', blank=True, null=True)
    description = models.TextField(_('Description'))
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(Participant, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('event-list')
