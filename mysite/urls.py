from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead,first,sec,new,base,section,search_form,search,search1_form,search1,search2,contact,thanks
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^first/',first),url(r'^sec/',sec),url(r'^new/',new),
    url(r'^base/',base),url(r'^section/',section),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', hello),
    url(r'^time/',current_datetime),
    url(r'^another-time-page/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^search-form/',search_form),
    url(r'^search/',search),
    url(r'^search1-form/',search1_form),
    url(r'^search1/',search1),
    url(r'^search2/',search2),
    url(r'^contact-form/',contact),
    url(r'^thanks/',thanks),
    url(r'^student/', include('student.urls')),
)
