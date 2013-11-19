# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from .models import Topic, Service, Client

urlpatterns = patterns(
    '',
    url(
        r'^topic/(?P<slug>[\w-]+)/$',
        DetailView.as_view(
            model=Topic,
            template_name='cmsplugin_featuresite/topic.html'),
        name='topic_detail'),
    url(
        r'^service/(?P<slug>[\w-]+)/$',
        DetailView.as_view(
            model=Service,
            template_name='cmsplugin_featuresite/service.html'),
        name='service_detail'),
    url(
        r'^client/(?P<slug>[\w-]+)/$',
        DetailView.as_view(
            model=Client,
            template_name='cmsplugin_featuresite/client.html'),
        name='client_detail'),
    url(
        r'^client/$',
        ListView.as_view(
            model=Client,
            template_name='cmsplugin_featuresite/client_list.html'),
        name='client_list'),
)
