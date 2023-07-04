from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    re_path(r'^delete/(?P<delete_id>[0-9]+$)', views.delete, name='delete'),
    re_path(r'^images/(?P<slugInput>[\w-]+$)', views.images2, name='images2'),
    re_path(r'^update/(?P<update_id>[0-9]+$)', views.update, name='update'),
    re_path(r'^add$', views.add, name='add'),
    re_path(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
