from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'concours'

urlpatterns = [

    # Administration
    url(r'^admin/', admin.site.urls),

    # Concours
    url(r'^miss/$', views.miss, name='miss'),
    url(r'^$', views.index, name='index'),


]