from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import FeaturePlugin
from .models import Topic, TopicPlugin
from .models import ServicePlugin
from .models import Client, ClientPlugin


class CMSFeaturePlugin(CMSPluginBase):
    model = FeaturePlugin
    name = _('Feature')
    render_template = "cmsplugin_featuresite/cms_feature.html"

    def render(self, context, instance, placeholder):
        feature = instance.feature
        context.update({
            'feature': feature
        })
        return context


class CMSTopicPlugin(CMSPluginBase):
    model = TopicPlugin
    name = _('Topic')
    render_template = "cmsplugin_featuresite/cms_topic.html"

    def render(self, context, instance, placeholder):
        topic_list = Topic.objects.all()[:instance.limit]
        context.update({
            'topic_list': topic_list
        })
        return context


class CMSClientPlugin(CMSPluginBase):
    model = ClientPlugin
    name = _('Client')
    render_template = "cmsplugin_featuresite/cms_client.html"

    def render(self, context, instance, placeholder):
        client_list = Client.objects.all()[:instance.limit]
        context.update({
            'client_list': client_list
        })
        return context


class CMSServicePlugin(CMSPluginBase):
    model = ServicePlugin
    name = _('Service')
    render_template = "cmsplugin_featuresite/cms_service.html"

    def render(self, context, instance, placeholder):
        service = instance.service
        context.update({
            'service': service
        })
        return context

plugin_pool.register_plugin(CMSFeaturePlugin)
plugin_pool.register_plugin(CMSClientPlugin)
plugin_pool.register_plugin(CMSTopicPlugin)
plugin_pool.register_plugin(CMSServicePlugin)
