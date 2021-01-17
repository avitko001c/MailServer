from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mail.urls")),
    url(r'^rlogin/$', auth_views.LoginView, {'template_name': 'templates/login.html'}, name='rlogin'),
    url(r'^rlogout/$', auth_views.LogoutView, {'next_page': '/'}, name='rlogout'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
