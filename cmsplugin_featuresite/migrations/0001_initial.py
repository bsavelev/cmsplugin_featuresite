# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feature'
        db.create_table(u'cmsplugin_featuresite_feature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seo_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('seo_description', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('seo_keywords', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 19, 0, 0))),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_featuresite', ['Feature'])

        # Adding model 'FeaturePlugin'
        db.create_table(u'cmsplugin_featureplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_featuresite.Feature'])),
        ))
        db.send_create_signal(u'cmsplugin_featuresite', ['FeaturePlugin'])

        # Adding model 'Topic'
        db.create_table(u'cmsplugin_featuresite_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seo_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('seo_description', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('seo_keywords', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 19, 0, 0))),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_featuresite', ['Topic'])

        # Adding model 'TopicPlugin'
        db.create_table(u'cmsplugin_topicplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('limit', self.gf('django.db.models.fields.PositiveIntegerField')(default=3)),
        ))
        db.send_create_signal(u'cmsplugin_featuresite', ['TopicPlugin'])

        # Adding model 'Service'
        db.create_table(u'cmsplugin_featuresite_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seo_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('seo_description', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('seo_keywords', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 19, 0, 0))),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_featuresite', ['Service'])

        # Adding model 'ServicePlugin'
        db.create_table(u'cmsplugin_serviceplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_featuresite.Service'])),
        ))
        db.send_create_signal(u'cmsplugin_featuresite', ['ServicePlugin'])


    def backwards(self, orm):
        # Deleting model 'Feature'
        db.delete_table(u'cmsplugin_featuresite_feature')

        # Deleting model 'FeaturePlugin'
        db.delete_table(u'cmsplugin_featureplugin')

        # Deleting model 'Topic'
        db.delete_table(u'cmsplugin_featuresite_topic')

        # Deleting model 'TopicPlugin'
        db.delete_table(u'cmsplugin_topicplugin')

        # Deleting model 'Service'
        db.delete_table(u'cmsplugin_featuresite_service')

        # Deleting model 'ServicePlugin'
        db.delete_table(u'cmsplugin_serviceplugin')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_featuresite.feature': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'Feature'},
            'content': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 19, 0, 0)'}),
            'seo_description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'seo_keywords': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'cmsplugin_featuresite.featureplugin': {
            'Meta': {'object_name': 'FeaturePlugin', 'db_table': "u'cmsplugin_featureplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsplugin_featuresite.Feature']"})
        },
        u'cmsplugin_featuresite.service': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'Service'},
            'content': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 19, 0, 0)'}),
            'seo_description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'seo_keywords': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'cmsplugin_featuresite.serviceplugin': {
            'Meta': {'object_name': 'ServicePlugin', 'db_table': "u'cmsplugin_serviceplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsplugin_featuresite.Service']"})
        },
        u'cmsplugin_featuresite.topic': {
            'Meta': {'ordering': "('pub_date',)", 'object_name': 'Topic'},
            'content': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 19, 0, 0)'}),
            'seo_description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'seo_keywords': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'cmsplugin_featuresite.topicplugin': {
            'Meta': {'object_name': 'TopicPlugin', 'db_table': "u'cmsplugin_topicplugin'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'limit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3'})
        }
    }

    complete_apps = ['cmsplugin_featuresite']