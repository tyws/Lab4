from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *
#from Test.BookManagement import views
#from django.contrib import admin
#admin.autodiscover()
#change3

urlpatterns = patterns('BookManagement.views',
    # Examples:
    # url(r'^$', 'Test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Hello'),
    url(r'^books/', 'Books'),
    url(r'^book/(\d)', 'book'),
    url(r'^createbook/', 'CreateBook'),
    url(r'^createauthor/', 'CreateAuthor'),
    url(r'^update/(\d)', 'Update'),
)
