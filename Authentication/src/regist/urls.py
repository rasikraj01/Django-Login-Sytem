from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


from .views import UserFormView, LoginView, home, logout_view


urlpatterns = [
    url(r'^$', UserFormView.as_view(), name='registraion'),
    url(r'login/', LoginView.as_view(), name='login'),
    url(r'^home/$', home.as_view(), name='home'),
    url(r'^logout/$', logout_view, name='logout'),
    #url(r'success/', SuccessView.as_view(), name='sccuess')
]