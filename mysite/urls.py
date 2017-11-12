"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from mysite.views import current_datetime, hours_ahead, hello_pdf
from books import views as learn_views 

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='user'),
	url(r'^time/$', current_datetime, name='time'),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead, name='plus_time'),
	url(r'^$', learn_views.index, name='home'),
	url(r'^new_add/(\d+)/(\d+)/$', learn_views.add, name='add'),
	url(r'^search/$',learn_views.search),
	url(r'^contact/$', learn_views.contact),
	url(r'^hello/$', hello_pdf),
]
