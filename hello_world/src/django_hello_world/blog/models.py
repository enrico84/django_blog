# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Post(models.Model):
    '''Modello a oggetti di un blog'''
    
    autore = models.ForeignKey('auth.User')
    titolo = models.CharField(max_length=200)
    testo = models.TextField()
    data_creazione = models.DateTimeField(
            default=timezone.now)
    data_pubblicazione = models.DateTimeField(
            blank=True, null=True)

    def pubblica(self):
        '''Metodo che pubblica un post'''
        
        self.data_pubblicazione = timezone.now()
        self.save()


    def __str__(self):
        '''Torna il titolo del post'''
        return self.titolo
