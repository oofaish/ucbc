from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseNotFound
from django.http import Http404
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import ListView
from simple.models import Page, Category, Crew, Image
from django.template import loader, Context
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.conf import settings
import re
import json
from django.db.models import Q
import markdown
from django import template

from filebrowser.sites import site
from filebrowser.base import FileListing
from filebrowser.base import FileObject
from filebrowser.settings import DIRECTORY as FB_DIRECTORY
from os.path import join

from random import shuffle
from random import randint

class ContactForm( forms.Form ):
    defaultAttr = [ ( 'required', '' ), ( 'class', 'input' ) ]

    subject     = forms.CharField( max_length=100, widget = forms.TextInput(attrs = dict( defaultAttr + [ ( 'placeholder', 'Subject' ) ] ) ) )
    message     = forms.CharField( max_length=1000, widget = forms.Textarea(attrs=dict( defaultAttr + [ ( 'placeholder', 'Message' ) ] ) ), label="Message" )
    sendername  = forms.CharField( max_length=100, label="Name", widget = forms.TextInput(attrs=dict( defaultAttr + [ ( 'placeholder', 'Your Name' ) ] ) ) )
    senderemail = forms.EmailField( label="Email", widget = forms.TextInput(attrs=dict( defaultAttr + [ ( 'placeholder', 'Your Email' ) ]  ) ) )

def ensurePermission( page, request ):
    if page.status == 0 and not request.user.is_authenticated():
        raise PermissionDenied

def getImage( originalImage, size ):
    if size:
        imageURL = loader.render_to_string( 'simple/subs/image.html', { 'fileObject': originalImage, 'size': size } )
    else:
        imageURL = loader.render_to_string( 'simple/subs/image.html', { 'fileObject': originalImage } )
    return imageURL.strip()

def paragraphedPageContent( page, includeImages = True, stopAt = None ):
    content = page.content1
    imageTagsAndLocations = re.findall( r'\[\[([\w\s/\\]*);([\w\s/\\]*)(;*[\w\s/\\]*)\]\]', content )
    for (imageTag,imageLocation,imageSize) in imageTagsAndLocations:
        imageSizeOriginal = imageSize
        if includeImages:
            if len( imageSize ) == 1:
                imageSize = None
            elif len( imageSize ) == 0:
                imageSize = 'medium'
            else:
                imageSize = imageSize[1:].lower()
            if imageLocation == 'left' or imageLocation == 'right':
                css = "display:block; float:" + imageLocation
                captionCss = "text-align:left"
            elif imageLocation == 'center' or imageLocation=='centre':
                css="display:block; margin-left:auto; margin-right:auto"
                captionCss = 'text-align:center'
            else:
                css = ''
                captionCss = ''
            try:
                try:
                    imageInstance = page.images.get(title=imageTag)
                except:
                    imageInstance = get_object_or_404( Image, title=imageTag )

                if imageInstance.imageFile.is_version:
                    originalImage = imageInstance.imageFile.original
                else:
                    originalImage = imageInstance.imageFile
                if originalImage.exists:
                    imageURL = getImage( originalImage, imageSize )

                    if len( imageInstance.caption ) > 0:
                        if imageLocation == 'center' or imageLocation=='centre':
                            newImageTag = '<img style="' + css + '" src="' + imageURL + '" alt="'+ imageInstance.title + '">'
                        else:
                            newImageTag = '<img src="' + imageURL + '" alt="'+ imageInstance.title + '">'
                        newImageTag = '<figure style="' + css + '">' +newImageTag + '<figcaption style="' + captionCss + '"><i>' + imageInstance.caption + '</i></figcaption></figure>'
                    else:
                        newImageTag = '<img style="' + css + '" src="' + imageURL + '" alt="'+ imageInstance.title + '">'
                    content = content.replace( '[[' + imageTag + ';' + imageLocation + imageSizeOriginal + ']]', newImageTag )
                else:
                    print 'File does not exist for tag: ', imageTag
            except Exception as inst:
                print 'Failed to get image ', imageTag, ':', inst
        else:
            content = content.replace( '[[' + imageTag + ';' + imageLocation + imageSizeOriginal + ']]', '' )

    if stopAt != None:
        totalLength = len( content )
        content = content[ 0:min( stopAt , len( content ) ) ]
        if stopAt < totalLength:
            content = content + ' ....'

    return markdown.markdown( content )

def extraContextItems():
    form = ContactForm()

    #page     = Page.objects.get(slug='news')
    posts    = Page.objects.filter(status=1,categories__name='newspost' ).order_by( '-created' )
    maxPosts = min( len( posts ), 8 )
    posts    = posts[0:maxPosts-1]

    postsToPrint = []

    for post in posts:
        postDic = {}
        postDic[ 'title' ] = post.title
        postDic[ 'year' ]  = post.created.year
        postDic[ 'slug' ]  = post.slug
        images = post.images.all()
        postDic[ 'image' ] = '/media/uploads/siteStatic/crest.png'
        foundImage = False

        if len( images ) > 0:
            i = randint( 0, len( images ) - 1 )
            foundImage = True
            imageFile = images[ i ].imageFile
        else:
            crews = post.crew_set.all()
            if len( crews ) > 0:
                is1 = range( 0, len( crews ) )
                shuffle( is1 )
                for i in is1:
                    images = crews[ i ].images.all()
                    if len( images ) > 0:
                        i = randint( 0, len( images ) - 1 )
                        foundImage = True
                        imageFile = images[ i ].imageFile
                        break

        if foundImage:
            if imageFile.is_version:
                originalImage = imageFile.original
            else:
                originalImage = imageFile
            mediumURL = getImage( originalImage, 'medium' )

            postDic[ 'image' ] = mediumURL

        postsToPrint.append( postDic )

    templateName = 'simple/subs/sideNews.html'
    sideNews = loader.render_to_string( templateName, { 'posts': postsToPrint } )

    try:
        footerPage = Page.objects.get(slug='hidden-footer')
        footer = paragraphedPageContent( footerPage )
    except:
        footer = 'the boat club president is a nerd'

    try:
        navPage = Page.objects.get(slug='navs')
        navs = navPage.content1
    except:
        navs = 'Menus Not Found'

    return [( 'contactform', form ), ( 'footer', footer ), ('sideNews', sideNews ), ('navs', navs ) ]

def renderWithDefaults( request, context ):

    extras = extraContextItems()
    newContext = dict(  context.items() + extras )
    return render( request, 'simple/page.html', newContext )


def catPageViewStuff( category, year, slug, json, request ):
    ensureList( category )

    myCat = Category.objects.get(name=category).subCategoryName
    page = get_object_or_404( Page, slug=slug, created__year=year, categories__name=myCat )

    ensurePermission( page, request )

    if json:
        returnDic = page.pageDict()
    else:
        returnDic = {'page':page}

    templateName = 'simple/subs/' + myCat + '.html'
    pageContent = paragraphedPageContent( page )

    returnDic[ 'htmlContent' ] = loader.render_to_string( templateName, { 'page': page, 'pageContent': pageContent, 'path': request.path } )

    return returnDic

def catPageView( request, category, year, slug ):
    context = catPageViewStuff( category, year, slug, False, request )
    return renderWithDefaults( request, context )

def catPageViewJson( request, category, year, slug ):
    returnDic = catPageViewStuff( category, year, slug, True, request )
    return HttpResponse( json.dumps( returnDic , cls=DjangoJSONEncoder), content_type = 'application/json' )

def ensureList( category ):
    category = Category.objects.get(name=category)
    if len( category.subCategoryName ) == 0:
        raise Http404

def imagesFromSubfolder( subfolder ):

    directory = FB_DIRECTORY

    path = u'%s' % join( directory, 'gallery', subfolder )

    filelisting = FileListing(
        path,
        #filter_func=filter_browse,
        sorting_by='name',
        sorting_order='desc',
        #site=self
        )

    images = []

    for fileObject in filelisting.files_walk_filtered():#files_walk_total():
        image = {}
        if fileObject.width != None:
            thumbnail = getImage( fileObject, 'thumbnail' )
            fileName  = fileObject.url
            #thumbnail = loader.render_to_string( 'simple/subs/image.html', { 'fileObject': fileObject, 'size': 'thumbnail' } )
            #fileName  = loader.render_to_string( 'simple/subs/image.html', { 'fileObject': fileObject } )
            image[ 'url' ] = fileName
            image[ 'thumbnailUrl' ] = thumbnail
            image[ 'title' ] = fileObject.filename_root
            images.append( image )
    return images;

def albumView( request, category, album ):
    page = get_object_or_404( Page, slug=album, categories__name='album' )
    ensurePermission( page, request )
    context = {'page':page}

    images = imagesFromSubfolder( album )
    shuffle( images )
    templateName = 'simple/subs/album.html'
    pageContent = paragraphedPageContent( page );
    context[ 'htmlContent' ] = loader.render_to_string( templateName, { 'page': page, 'pageContent': pageContent, 'images': images} )

    return renderWithDefaults( request, context )

def crewView( request, pk ):
    crew = get_object_or_404( Crew, id=pk )

    context0 = {'page':crew}
    context = {}

    if crew.boatClass.name[ 0 ] == '8':
        seats = [ 'Bow', 2, 3, 4, 5, 6, 7, 'Stroke' ]
    elif crew.boatClass.name == '1x':
        seats = [ 'Sculler' ]
    elif crew.boatClass.name[ 0 ] == '2':
        seats = [ 'Bow', 'Stroke' ]
    elif crew.boatClass.name[ 0 ] == '4':
        seats = [ 'Bow', 2, 3, 'Stroke' ]
    else:
        seats = []

    numSeats = len( seats )
    members  = ['The Master'] * numSeats

    if numSeats > 0:
        if crew.seat1:
            members[ 0 ] = crew.seat1
    if numSeats > 1:
        if crew.seat2:
            members[ 1 ] = crew.seat2
    if numSeats > 3:
        if crew.seat3:
            members[ 2 ] = crew.seat3
        if crew.seat4:
            members[ 3 ] = crew.seat4
    if numSeats > 4:
        if crew.seat5:
            members[ 4 ] = crew.seat5
        if crew.seat6:
            members[ 5 ] = crew.seat6
        if crew.seat7:
            members[ 6 ] = crew.seat7
        if crew.seat8:
            members[ 7 ] = crew.seat8

    images = []

    for imageObject in crew.images.all():
        fileObject = imageObject.imageFile
        image = {}
        image[ 'url' ] = fileObject.original.url;
        thumbnail = getImage( fileObject, 'thumbnail' )
        #thumbnail = loader.render_to_string( 'simple/subs/image.html', { 'fileObject': fileObject, 'size': 'thumbnail' } )
        image[ 'thumbnailUrl' ] = thumbnail
        image[ 'title' ] = fileObject.filename_root
        images.append( image )

    context[ 'seats'   ] = zip( seats, members )
    context[ 'images' ] = images
    context[ 'crew'     ] = crew
    context[ 'pageContent' ] = paragraphedPageContent( crew );
    templateName = 'simple/subs/crew.html'
    context0[ 'htmlContent' ] = loader.render_to_string( templateName, context )

    return renderWithDefaults( request, context0 )

def crewsView( request, category ):
    page = get_object_or_404( Page, categories__name='crews' )
    ensurePermission( page, request )

    context = {'page':page}

    crews = Crew.objects.filter(status=1 ).order_by( '-season__startYear', 'boatNumber__number', '-boatNumber__sex' )
    seasons = [];
    for crew in crews:
        if not crew.season.title in seasons:
            seasons.append( crew.season.title )

    emptyListHack = [];

    crewsBySeason = zip( seasons, [ emptyListHack[:] for x in range( len( seasons ) ) ] )
    compsBySeason = zip( seasons, [ emptyListHack[:] for x in range( len( seasons ) ) ] )

    for crew in crews:
        i = seasons.index( crew.season.title )
        if not crew.competition.name in compsBySeason[ i ][ 1 ]:
            compsBySeason[ i ][ 1 ].append( crew.competition.name )
            crewsBySeason[ i ][ 1 ].append( ( crew.competition.name, [] ) )
        j = compsBySeason[ i ][ 1 ].index( crew.competition.name )
        crewsBySeason[ i ][ 1 ][ j ][ 1 ].append( crew )

    templateName = 'simple/subs/crews.html'
    pageContent = paragraphedPageContent( page );
    context[ 'htmlContent' ] = loader.render_to_string( templateName, { 'page': page, 'pageContent': pageContent, 'crewsBySeason': crewsBySeason } )

    return renderWithDefaults( request, context )

def listViewStuff( category, json, request ):
    ensureList( category )
    page = Page.objects.get(slug=category)
    ensurePermission( page, request )
    posts = Page.objects.filter(status=1,categories__name=page.categories.all()[ 0 ].subCategoryName ).order_by( '-created' )

    postDics = []
    for post in posts:
        postDic = {}
        postDic[    'post' ] = post
        summary = paragraphedPageContent( post, includeImages = False, stopAt = 600 )

        postDic[ 'summary' ] = summary
        postDics.append( postDic )
    if json:
        returnDic = page.pageDict()
    else:
        returnDic = {'page':page}

    templateName = 'simple/subs/' + category + '.html'
    pageContent = paragraphedPageContent( page );
    returnDic[ 'htmlContent' ] = loader.render_to_string( templateName, { 'page': page, 'pageContent':pageContent, 'postDics': postDics } )

    return returnDic

def listView( request, category ):
    context = listViewStuff( category, False, request )
    return renderWithDefaults( request, context )

def listViewJson( request, category ):
    returnDic = listViewStuff( category, True, request )
    return HttpResponse( json.dumps( returnDic , cls=DjangoJSONEncoder), content_type = 'application/json' )


def staticViewInstance( request, slug ):
    try:
        #pageInstance = Page.objects.get(slug=slug).
        pageInstance = Page.objects.filter(slug=slug).filter(Q(categories__name='static') | Q(categories__name='gallery')).all()
        if len( pageInstance ) != 1:
            raise Http404
        pageInstance = pageInstance[ 0 ]
        ensurePermission( pageInstance, request )
    except Page.DoesNotExist:
        raise Http404

    return pageInstance

def staticViewJson( request, slug='home' ):
    pageInstance = staticViewInstance( request, slug )
    returnDic = pageInstance.pageDict()
    pageContent = paragraphedPageContent( pageInstance );
    returnDic[ 'htmlContent' ] = loader.render_to_string( 'simple/subs/static.html', {'pageContent':pageContent })

    return HttpResponse( json.dumps( returnDic , cls=DjangoJSONEncoder), content_type = 'application/json' )

def staticView( request, slug='home' ):
    pageInstance = staticViewInstance( request, slug )
    pageContent = paragraphedPageContent( pageInstance );
    html = loader.render_to_string( 'simple/subs/static.html', {'pageContent':pageContent})

    return renderWithDefaults( request, {'page': pageInstance, 'htmlContent': html } )

def submitContactForm( request ):
    if request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            subject     = form.cleaned_data[     'subject' ]
            message     = form.cleaned_data[     'message' ]
            sendername  = form.cleaned_data[  'sendername' ]
            senderemail = form.cleaned_data[ 'senderemail' ]
            recipients = [ x[ 1 ] for x in settings.ADMINS ]
            messageText = 'From: %s (%s)\n--------\n%s'%(sendername, senderemail,message)
            send_mail(subject , messageText, senderemail, recipients )
            return HttpResponse( json.dumps( {'done':True } ), content_type = 'application/json' )
        else:
            return HttpResponse( json.dumps( {'error':form.errors } ), content_type = 'application/json' )
    else:
        raise Http404

def handler404(request):
    extras = extraContextItems()
    html = loader.render_to_string( 'simple/404.html', dict( extras ) )
    return HttpResponseNotFound(html)

def handler403(request):
    extras = extraContextItems()
    html = loader.render_to_string( 'simple/403.html', dict( extras ) )
    return HttpResponseNotFound(html)
