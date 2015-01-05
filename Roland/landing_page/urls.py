from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='home'),
    url(r'^defaultsite$', views.index, name='home'),
    url(r'^partitioning$',views.partitioning, name='partitioning'),
    url(r'^ceilings$',views.ceilings, name='celings'),
    url(r'^other$',views.other, name='other'),
    url(r'^endorsements$',views.endorsements, name='endorsements'),
)