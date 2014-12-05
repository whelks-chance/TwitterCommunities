__author__ = 'ubuntu'
from django.conf.urls import patterns, include, url
from overlaps import views

urlpatterns = patterns('',
                       url(r'^$', 'overlaps.views.home', name='overlaps.home'),
                       url(r'^twitter_compare', 'overlaps.views.twitter_compare', name='overlaps.twitter_compare'),

                       )