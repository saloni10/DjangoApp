from django.conf.urls import patterns, include, url

from student import views

urlpatterns = patterns('',
    url(r'^fee/', views.fee,name='fee' ),
    # url(r'^fee/',fee ),
    url(r'^form/', views.form,name='form'),
)
