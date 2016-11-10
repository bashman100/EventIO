"""eventio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth.views import login, logout
from accounts.views import register_user
from events.views import index, event_details, event_add, event_edit, event_delete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^event/(?P<pk>\d+)/$', event_details, name='event'),
    url(r'^event/add/$', event_add, name='event_add'),
    url(r'^event/(?P<pk>\d+)/edit/$', event_edit, name='event_edit'),
    url(r'^event/(?P<pk>\d+)/delete/$', event_delete, name='event_delete'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', register_user, name="register"),
]
