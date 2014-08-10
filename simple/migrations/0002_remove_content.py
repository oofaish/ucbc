# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'simple_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('subCategoryName', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'simple', ['Category'])

        # Adding model 'Script'
        db.create_table(u'simple_script', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'simple', ['Script'])

        # Adding model 'Stylesheet'
        db.create_table(u'simple_stylesheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'simple', ['Stylesheet'])

        # Adding model 'Tag'
        db.create_table(u'simple_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'simple', ['Tag'])

        # Adding model 'Image'
        db.create_table(u'simple_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imageFile', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
        ))
        db.send_create_signal(u'simple', ['Image'])

        # Adding model 'Page'
        db.create_table(u'simple_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 8, 10, 0, 0))),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('kudos', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('showKudos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reads', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('inlinescript', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('inlinestyle', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'simple', ['Page'])

        # Adding M2M table for field categories on 'Page'
        m2m_table_name = db.shorten_name(u'simple_page_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'simple.page'], null=False)),
            ('category', models.ForeignKey(orm[u'simple.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'category_id'])

        # Adding M2M table for field tags on 'Page'
        m2m_table_name = db.shorten_name(u'simple_page_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'simple.page'], null=False)),
            ('tag', models.ForeignKey(orm[u'simple.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'tag_id'])

        # Adding M2M table for field images on 'Page'
        m2m_table_name = db.shorten_name(u'simple_page_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'simple.page'], null=False)),
            ('image', models.ForeignKey(orm[u'simple.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'image_id'])

        # Adding M2M table for field stylesheets on 'Page'
        m2m_table_name = db.shorten_name(u'simple_page_stylesheets')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'simple.page'], null=False)),
            ('stylesheet', models.ForeignKey(orm[u'simple.stylesheet'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'stylesheet_id'])

        # Adding M2M table for field scripts on 'Page'
        m2m_table_name = db.shorten_name(u'simple_page_scripts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'simple.page'], null=False)),
            ('script', models.ForeignKey(orm[u'simple.script'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'script_id'])

        # Adding model 'Role'
        db.create_table(u'simple_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'simple', ['Role'])

        # Adding model 'Boat'
        db.create_table(u'simple_boat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('priority', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'simple', ['Boat'])

        # Adding model 'BoatType'
        db.create_table(u'simple_boattype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('seats', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=8)),
            ('coxless', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'simple', ['BoatType'])

        # Adding model 'CommitteeRoleTitle'
        db.create_table(u'simple_committeeroletitle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'simple', ['CommitteeRoleTitle'])

        # Adding model 'Competition'
        db.create_table(u'simple_competition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'simple', ['Competition'])

        # Adding model 'Term'
        db.create_table(u'simple_term', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'simple', ['Term'])

        # Adding model 'Season'
        db.create_table(u'simple_season', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('startYear', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('endYear', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('titleInternal', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'simple', ['Season'])

        # Adding model 'CommitteeRole'
        db.create_table(u'simple_committeerole', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple.CommitteeRoleTitle'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple.Season'])),
        ))
        db.send_create_signal(u'simple', ['CommitteeRole'])

        # Adding model 'Member'
        db.create_table(u'simple_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'simple', ['Member'])

        # Adding M2M table for field roles on 'Member'
        m2m_table_name = db.shorten_name(u'simple_member_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'simple.member'], null=False)),
            ('role', models.ForeignKey(orm[u'simple.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'role_id'])

        # Adding M2M table for field committeeRoles on 'Member'
        m2m_table_name = db.shorten_name(u'simple_member_committeeRoles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'simple.member'], null=False)),
            ('committeerole', models.ForeignKey(orm[u'simple.committeerole'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'committeerole_id'])

        # Adding M2M table for field images on 'Member'
        m2m_table_name = db.shorten_name(u'simple_member_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'simple.member'], null=False)),
            ('image', models.ForeignKey(orm[u'simple.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'image_id'])

        # Adding model 'Crew'
        db.create_table(u'simple_crew', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple.Season'])),
            ('boat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple.Boat'], null=True, blank=True)),
            ('boatType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple.BoatType'], null=True, blank=True)),
            ('competition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple.Competition'], null=True, blank=True)),
            ('Term', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple.Term'], null=True, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('priority', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('seat1', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='seat1s', null=True, to=orm['simple.Member'])),
            ('seat2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='seat2s', null=True, to=orm['simple.Member'])),
            ('seat3', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='seat3s', null=True, to=orm['simple.Member'])),
            ('seat4', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='seat4s', null=True, to=orm['simple.Member'])),
            ('seat5', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='seat5s', null=True, to=orm['simple.Member'])),
            ('seat6', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='seat6s', null=True, to=orm['simple.Member'])),
            ('seat7', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='seat7s', null=True, to=orm['simple.Member'])),
            ('seat8', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='seat8s', null=True, to=orm['simple.Member'])),
        ))
        db.send_create_signal(u'simple', ['Crew'])

        # Adding M2M table for field reports on 'Crew'
        m2m_table_name = db.shorten_name(u'simple_crew_reports')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crew', models.ForeignKey(orm[u'simple.crew'], null=False)),
            ('page', models.ForeignKey(orm[u'simple.page'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crew_id', 'page_id'])

        # Adding M2M table for field images on 'Crew'
        m2m_table_name = db.shorten_name(u'simple_crew_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crew', models.ForeignKey(orm[u'simple.crew'], null=False)),
            ('image', models.ForeignKey(orm[u'simple.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crew_id', 'image_id'])

        # Adding M2M table for field subs on 'Crew'
        m2m_table_name = db.shorten_name(u'simple_crew_subs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crew', models.ForeignKey(orm[u'simple.crew'], null=False)),
            ('member', models.ForeignKey(orm[u'simple.member'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crew_id', 'member_id'])

        # Adding M2M table for field coxes on 'Crew'
        m2m_table_name = db.shorten_name(u'simple_crew_coxes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crew', models.ForeignKey(orm[u'simple.crew'], null=False)),
            ('member', models.ForeignKey(orm[u'simple.member'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crew_id', 'member_id'])

        # Adding M2M table for field coaches on 'Crew'
        m2m_table_name = db.shorten_name(u'simple_crew_coaches')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crew', models.ForeignKey(orm[u'simple.crew'], null=False)),
            ('member', models.ForeignKey(orm[u'simple.member'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crew_id', 'member_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'simple_category')

        # Deleting model 'Script'
        db.delete_table(u'simple_script')

        # Deleting model 'Stylesheet'
        db.delete_table(u'simple_stylesheet')

        # Deleting model 'Tag'
        db.delete_table(u'simple_tag')

        # Deleting model 'Image'
        db.delete_table(u'simple_image')

        # Deleting model 'Page'
        db.delete_table(u'simple_page')

        # Removing M2M table for field categories on 'Page'
        db.delete_table(db.shorten_name(u'simple_page_categories'))

        # Removing M2M table for field tags on 'Page'
        db.delete_table(db.shorten_name(u'simple_page_tags'))

        # Removing M2M table for field images on 'Page'
        db.delete_table(db.shorten_name(u'simple_page_images'))

        # Removing M2M table for field stylesheets on 'Page'
        db.delete_table(db.shorten_name(u'simple_page_stylesheets'))

        # Removing M2M table for field scripts on 'Page'
        db.delete_table(db.shorten_name(u'simple_page_scripts'))

        # Deleting model 'Role'
        db.delete_table(u'simple_role')

        # Deleting model 'Boat'
        db.delete_table(u'simple_boat')

        # Deleting model 'BoatType'
        db.delete_table(u'simple_boattype')

        # Deleting model 'CommitteeRoleTitle'
        db.delete_table(u'simple_committeeroletitle')

        # Deleting model 'Competition'
        db.delete_table(u'simple_competition')

        # Deleting model 'Term'
        db.delete_table(u'simple_term')

        # Deleting model 'Season'
        db.delete_table(u'simple_season')

        # Deleting model 'CommitteeRole'
        db.delete_table(u'simple_committeerole')

        # Deleting model 'Member'
        db.delete_table(u'simple_member')

        # Removing M2M table for field roles on 'Member'
        db.delete_table(db.shorten_name(u'simple_member_roles'))

        # Removing M2M table for field committeeRoles on 'Member'
        db.delete_table(db.shorten_name(u'simple_member_committeeRoles'))

        # Removing M2M table for field images on 'Member'
        db.delete_table(db.shorten_name(u'simple_member_images'))

        # Deleting model 'Crew'
        db.delete_table(u'simple_crew')

        # Removing M2M table for field reports on 'Crew'
        db.delete_table(db.shorten_name(u'simple_crew_reports'))

        # Removing M2M table for field images on 'Crew'
        db.delete_table(db.shorten_name(u'simple_crew_images'))

        # Removing M2M table for field subs on 'Crew'
        db.delete_table(db.shorten_name(u'simple_crew_subs'))

        # Removing M2M table for field coxes on 'Crew'
        db.delete_table(db.shorten_name(u'simple_crew_coxes'))

        # Removing M2M table for field coaches on 'Crew'
        db.delete_table(db.shorten_name(u'simple_crew_coaches'))


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
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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