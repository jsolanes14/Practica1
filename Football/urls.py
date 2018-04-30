"""Football URL Configuration

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
from django.contrib.auth.views import login, logout

import footballRates.views as fv

urlpatterns = [
    url(r'^matches/', fv.MatchListView.as_view(), name='Match'),
    url(r'^pronostics/', fv.PronosticListView.as_view(), name='Pronostic'),
    url(r'^', admin.site.urls),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),

]
