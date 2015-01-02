from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='home'),
    url(r'^partitioning$',views.partitioning, name='partitioning'),
    url(r'^ceilings$',views.ceilings, name='celings'),
    url(r'^mezzanine$',views.mezzanine, name='mezzanine'),
    url(r'^electrics$',views.electrics, name='electrics'),
    url(r'^office$',views.office, name='office'),
    url(r'^drylining$',views.drylining, name='drylining'),
    url(r'^decoration$',views.decoration, name='decoration'),
     url(r'^heating$',views.heating, name='heating'),
    # url(r'^other$',views.other, name='other'),
    # url(r'^endorsements$',views.endorsements, name='endorsements'),
)