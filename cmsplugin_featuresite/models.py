# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from cms.models import CMSPlugin
from tinymce.models import HTMLField


class BaseModel(models.Model):
    """
    Родительская модель для сео, Мета теги и title

    Поля:
    seo_title - title страницы
    seo_description - мета тег description
    seo_keywords - мета тег keywords
    """

    seo_title = models.CharField(max_length=100, verbose_name=_('SEO title'), null=True, blank=True)
    seo_description = models.CharField(max_length=250, verbose_name=_('SEO description'), null=True, blank=True)
    seo_keywords = models.CharField(max_length=250, verbose_name=_('SEO keywords'), null=True, blank=True)
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(
        _('Slug'), max_length=50,
        help_text=_('Short name which uniquely identifies the item'))
    content = HTMLField(_('Content'), blank=True)
    pub_date = models.DateTimeField(_('Publication date'), default=datetime.datetime.now())
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        ordering = ('pub_date',)

    def __unicode__(self):
        return self.title


class Feature(BaseModel):
    pass


class FeaturePlugin(CMSPlugin):
    feature = models.ForeignKey('Feature')


class Topic(BaseModel):
    def get_absolute_url(self):
        return reverse('topic_detail', args=[str(self.slug)])


class TopicPlugin(CMSPlugin):
    limit = models.PositiveIntegerField(_('Number of items to show'), default=3,
                                        help_text=_('Limits the number of items that will be displayed'))


class Service(BaseModel):
    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.slug)])


class ServicePlugin(CMSPlugin):
    service = models.ForeignKey('Service')


class Client(BaseModel):
    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.slug)])

    def main_photo(self):
        photo = self.clientphoto_set.all()
        if photo.exists():
            photo = photo[0].image
        else:
            photo = None
        return photo


class ClientPhoto(models.Model):
    project = models.ForeignKey('Client')
    image = models.ImageField(upload_to='client')


class ClientPlugin(CMSPlugin):
    limit = models.PositiveIntegerField(_('Number of items to show'), default=3,
                                        help_text=_('Limits the number of items that will be displayed'))
