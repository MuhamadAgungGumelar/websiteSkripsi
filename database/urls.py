from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    url(r'^delete/(?P<delete_id>[0-9]+$)', views.delete, name='delete'),
    url(r'^images/(?P<slugInput>[\w-]+$)', views.images2, name='images2'),
    url(r'^update/(?P<update_id>[0-9]+$)', views.update, name='update'),
    # url(r'^images/(?P<slugInput>[\w-]+$)', views.images, name='images'),
    url(r'^add$', views.add, name='add'),
    url(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA, document_root=settings.MEDIA_ROOT)





# url(r'^create/POST(?P<slug>[\w~]+)$', views.create),
# url(r'^create/$', views.create, name='create'),