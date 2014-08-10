# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Crew.content'
        db.delete_column(u'simple_crew', 'content')


    def backwards(self, orm):
        # Adding field 'Crew.content'
        db.add_column(u'simple_crew', 'content',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    models = {
        u'simple.boat': {
            'Meta': {'object_name': 'Boat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'priority': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'simple.boattype': {
            'Meta': {'object_name': 'BoatType'},
            'coxless': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'seats': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '8'})
        },
        u'simple.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subCategoryName': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'simple.committeerole': {
            'Meta': {'object_name': 'CommitteeRole'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple.Season']"}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple.CommitteeRoleTitle']"})
        },
        u'simple.committeeroletitle': {
            'Meta': {'object_name': 'CommitteeRoleTitle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'simple.competition': {
            'Meta': {'object_name': 'Competition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'simple.crew': {
            'Meta': {'object_name': 'Crew'},
            'Term': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple.Term']", 'null': 'True', 'blank': 'True'}),
            'boat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple.Boat']", 'null': 'True', 'blank': 'True'}),
            'boatType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple.BoatType']", 'null': 'True', 'blank': 'True'}),
            'coaches': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'coaches'", 'blank': 'True', 'to': u"orm['simple.Member']"}),
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple.Competition']", 'null': 'True', 'blank': 'True'}),
            'coxes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'coxes'", 'blank': 'True', 'to': u"orm['simple.Member']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['simple.Image']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'priority': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'reports': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['simple.Page']", 'symmetrical': 'False', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['simple.Season']"}),
            'seat1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seat1s'", 'null': 'True', 'to': u"orm['simple.Member']"}),
            'seat2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seat2s'", 'null': 'True', 'to': u"orm['simple.Member']"}),
            'seat3': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seat3s'", 'null': 'True', 'to': u"orm['simple.Member']"}),
            'seat4': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seat4s'", 'null': 'True', 'to': u"orm['simple.Member']"}),
            'seat5': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seat5s'", 'null': 'True', 'to': u"orm['simple.Member']"}),
            'seat6': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seat6s'", 'null': 'True', 'to': u"orm['simple.Member']"}),
            'seat7': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seat7s'", 'null': 'True', 'to': u"orm['simple.Member']"}),
            'seat8': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'seat8s'", 'null': 'True', 'to': u"orm['simple.Member']"}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'subs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'subs'", 'blank': 'True', 'to': u"orm['simple.Member']"}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'simple.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageFile': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'simple.member': {
            'Meta': {'object_name': 'Member'},
            'committeeRoles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['simple.CommitteeRole']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['simple.Image']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['simple.Role']", 'symmetrical': 'False', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'simple.page': {
            'Meta': {'object_name': 'Page'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['simple.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 10, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['simple.Image']", 'symmetrical': 'False', 'blank': 'True'}),
            'inlinescript': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'inlinestyle': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'kudos': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'reads': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'scripts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['simple.Script']", 'symmetrical': 'False', 'blank': 'True'}),
            'showKudos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'stylesheets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['simple.Stylesheet']", 'symmetrical': 'False', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['simple.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'simple.role': {
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'simple.script': {
            'Meta': {'object_name': 'Script'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'simple.season': {
            'Meta': {'object_name': 'Season'},
            'endYear': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'startYear': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'titleInternal': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'simple.stylesheet': {
            'Meta': {'object_name': 'Stylesheet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'simple.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'simple.term': {
            'Meta': {'object_name': 'Term'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['simple']