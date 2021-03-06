from django.db import models
import datetime
from django.utils import timezone
from datetime import datetime
from filebrowser.fields import FileBrowseField

class Category( models.Model ):
    name            = models.CharField( max_length=30 )
    subCategoryName = models.CharField( max_length=30, blank=True )

    def __unicode__(self):
        return self.name

class Script( models.Model ):
    name    = models.CharField( max_length = 30 )
    url     = models.URLField()

    def __unicode__(self):
        return self.name

class Stylesheet( models.Model ):
    name    = models.CharField( max_length = 30 )
    url     = models.URLField()

    def __unicode__(self):
        return self.name

class Tag( models.Model ):
    name = models.CharField( max_length=100 )

    def __unicode__(self):
        return self.name

class Image( models.Model ):
    imageFile = FileBrowseField(  "Image", max_length = 200, blank = True, null = True, format="image" )
    title     = models.CharField( max_length=100 )
    caption   = models.CharField( max_length=400, blank=True )

    def __unicode__(self):
        return self.title

def pageContentHelp():
    help = "<h2>Adding Images</h2><h3>Add an image by first adding it to the 'Images' section below. You can then include an image titled 'UCBCRocks' in the article by adding</h3>"
    help = help + '<h3>[[UCBCRocks;LOCATION;SIZE]],</h3><h3>to the article, where LOCATION could be left, right, center or left empty.</h3>'
    help = help + "<h3>And size can be 'thumbnail', 'small', 'medium', 'big' or 'large'</h3>"
    help = help + "<h3>Remember you can choose different sized images when selecting the image file by clicking the arrow on left hand side of the 'Select' Button.</h3>"
    return help

class Page( models.Model ):
    title         = models.CharField(max_length=200)
    slug          = models.CharField(max_length=30)
    content       = models.TextField(help_text = pageContentHelp() )
    categories    = models.ManyToManyField(Category, blank=True ) #'blogpost', 'static', 'idea',
    images        = models.ManyToManyField(Image, blank=True )
    tags          = models.ManyToManyField(Tag, blank=True ) #again for blog posts
    created       = models.DateTimeField(default=datetime.now())
    updated       = models.DateTimeField(auto_now=True)
    images        = models.ManyToManyField(Image, blank=True )
    stylesheets   = models.ManyToManyField(Stylesheet, blank=True )
    scripts       = models.ManyToManyField(Script, blank=True )
    inlinescript  = models.TextField(blank=True)
    inlinestyle   = models.TextField(blank=True)
    status        = models.PositiveSmallIntegerField(default=1)#0 means dont show it, 1 means show it
    password      = models.CharField(max_length=20,blank=True)

    @property
    def content1(self):
        return self.content

    def __unicode__( self ):
        if not self.status:
            return self.title + ' (Hidden)'
        else:
            return self.title + ' (Visible)'

    def pageDict( self ):
        keys = ( "title", "id", "kudos", "showKudos", 'inlinescript', 'inlinestyle' )
        r = {}

        for key in keys:
            r[ key ] = getattr( self, key )

        r[ 'longTitle' ] = self.longTitle

        scripts = []
        stylesheets = []
        for stylesheet in self.stylesheets.all():
            stylesheets.append(stylesheet.url)
        for script in self.scripts.all():
            scripts.append(script.url)

        r[ 'stylesheets' ] = stylesheets
        r[ 'scripts' ] = scripts

        return r

    @property
    def longTitle(self):
        return self.title

    @property
    def summary(self):
        return self.content[0:min(100,len(self.content))]

class BoatClass( models.Model ):
    name = models.CharField( max_length=20 )
    priority = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.name

class Role( models.Model ):
    name = models.CharField( max_length=50 )

    def __unicode__(self):
        return self.name

class BoatNumber( models.Model ):#M1, W2, etc
    sex    = models.CharField( max_length=1 )
    number = models.PositiveSmallIntegerField( default=1 )

    @property
    def title(self):
        return  self.sex + str( self.number )

    def __unicode__(self):
        return unicode( self.title )

class Boat( models.Model ):
    name = models.CharField( max_length=100, blank=True )
    make = models.CharField( max_length=50,blank=True )
    model = models.CharField(max_length=30, blank=True )
    weight = models.CharField( max_length=10, blank=True )
    notes = models.TextField(blank=True)
    year = models.PositiveIntegerField(default=0)
    boatClass = models.ForeignKey(BoatClass,null=True,blank=True)

    def __unicode__(self):
        return self.name

class CommitteeRoleTitle( models.Model ):
    name = models.CharField( max_length=50 )

    def __unicode__(self):
        return self.name

class Competition( models.Model ):
    name = models.CharField( max_length=50 )

    def __unicode__(self):
        return self.name

class Term( models.Model ):
    name = models.CharField( max_length=20 )

    def __unicode__(self):
        return self.name

class Season( models.Model ):
    startYear     = models.PositiveIntegerField(default=0)
    endYear       = models.PositiveIntegerField(default=0)
    titleInternal = models.CharField( max_length=50,blank=True)

    def __unicode__( self ):
        return unicode( self.title )

    @property
    def title(self):
        if len( self.titleInternal ) > 0:
            return self.titleInternal
        else:
            return str( self.startYear ) + '/' + str( self.endYear )

class CommitteeRole( models.Model ):
    title  = models.ForeignKey(CommitteeRoleTitle)
    season = models.ForeignKey( Season );

    def __unicode__(self):
        return self.title.name + ' ' + self.season.title

class Member( models.Model ):
    name           = models.CharField( max_length=100 )
    nickname       = models.CharField( max_length=50, blank = True  )
    summary        = models.TextField(blank=True)
    roles          = models.ManyToManyField(Role, blank=True )
    committeeRoles = models.ManyToManyField(CommitteeRole, blank=True )
    images         = models.ManyToManyField(Image, blank=True )
    status         = models.PositiveSmallIntegerField(default=1)#0 means dont show it, 1 means show it

    def __unicode__( self ):
        if not self.status:
            return self.name + ' (Hidden)'
        else:
            return self.name + ' (Visible)'

    @property
    def longTitle(self):
        return self.title

class Crew( models.Model ):
    name          = models.CharField( max_length=100, blank = True )
    season        = models.ForeignKey( Season )
    boatNumber    = models.ForeignKey(BoatNumber, null=True, blank=True)
    boat          = models.ForeignKey(Boat, null=True,blank=True)
    boatClass     = models.ForeignKey(BoatClass, null=True, blank=True)
    competition   = models.ForeignKey(Competition, null=True, blank=True)
    Term          = models.ForeignKey(Term, null=True, blank=True)
    summary       = models.TextField(blank=True)
    #content       = models.TextField(blank=True)
    reports       = models.ManyToManyField( Page,blank=True )
    images        = models.ManyToManyField(Image, blank=True )

    priority      = models.SmallIntegerField(default=0)
    status        = models.PositiveSmallIntegerField(default=1)#0 means dont show it, 1 means show it
    seat1         = models.ForeignKey(Member, null=True, blank=True, related_name='seat1s' )
    seat2         = models.ForeignKey(Member, null=True, blank=True, related_name='seat2s' )
    seat3         = models.ForeignKey(Member, null=True, blank=True, related_name='seat3s' )
    seat4         = models.ForeignKey(Member, null=True, blank=True, related_name='seat4s' )
    seat5         = models.ForeignKey(Member, null=True, blank=True, related_name='seat5s' )
    seat6         = models.ForeignKey(Member, null=True, blank=True, related_name='seat6s' )
    seat7         = models.ForeignKey(Member, null=True, blank=True, related_name='seat7s' )
    seat8         = models.ForeignKey(Member, null=True, blank=True, related_name='seat8s' )
    subs          = models.ManyToManyField(Member, blank=True, related_name='subs' )
    coxes         = models.ManyToManyField(Member, blank=True, related_name='coxes' )
    coaches       = models.ManyToManyField(Member, blank=True, related_name='coaches' )

    def __unicode__( self ):
        if not self.status:
            return self.name + ' - ' + self.season.title + ' (Hidden)'
        else:
            return self.name + ' - ' + self.season.title + ' (Visible)'
    @property
    def content1(self):
        return self.summary

    @property
    def shortTitle(self):
        r = '';
        if self.boatNumber:
            r = r + self.boatNumber.title

        if len( r ) == 0:
            r = '<unnamed>'
        return r

    @property
    def title(self):
        r = '';
        if self.boatNumber:
            r = r + ' ' + self.boatNumber.title
        if self.competition:
            r = r + ' ' + self.competition.name
        if self.season:
            r = r + ' ' + self.season.title
        if self.boatClass:
            r = r + ' (' + self.boatClass.name + ')'

        if len( r ) == 0:
            r = self.name
        return r

