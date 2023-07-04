from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views

from database.views import predictImage

from .views import index, Login, Logout, Registration

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^database/', include(('database.urls', 'database'), namespace='database')),
    re_path(r'^predictImage$', predictImage, name='predictImage'),
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(r'^Registration', Registration, name='registration'),
    re_path(r'^Logout$', Logout, name='logout'),
    re_path(r'^Login$', Login, name='login'),
    re_path(r'^$', index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
