"""
URL configuration for learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# your_app/urls.py
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include,  path

urlpatterns = [

    path('admin/', admin.site.urls),
    path('your_app/', include('your_app.urls')),


    path('form/', views.my_form_view, name='my_form'),
    path('success/', views.success_view, name='success'),  # Add a success view as well
    path('' , include('account.urls')),
]

