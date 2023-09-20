"""APITESCHI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import sing_in
from api.views import sing_up

urlpatterns = [
    #se comenta para que no se inicie con django directamente para así visualizar el trabajo que realizamos
    #path('admin/', admin.site.urls),
    #el siguiente comando se utiliza para que se visualice la ventana del index
    #path('',Home.as_view(),name='index'),
    path('sing_in/',sing_in.as_view(),name='sing_in'),
    path('sign_up/',sing_up.as_view(),name='sign_up'),
]
