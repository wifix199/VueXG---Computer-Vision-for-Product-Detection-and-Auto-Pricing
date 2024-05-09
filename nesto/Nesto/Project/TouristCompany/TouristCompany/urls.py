"""
URL configuration for TouristCompany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('paris.html', views.paris_view, name='paris'),
    path('index.html', views.gallery_view, name='gallery'),
    path('dubai.html', views.dubai_view, name='dubai'),
    path('singapore.html', views.singapore_view, name='singapore'),
    path('italy.html', views.italy_view, name='italy'),
    path('contact.html', views.contact_view, name='contact'),
    path('thailand.html', views.thailand_view, name='thailand'),
    path('maldives.html', views.maldives_view, name='maldives'),
    path('switzerland.html', views.switzerland_view, name='switzerland'),
    path('egypt.html', views.egypt_view, name='egypt'),
    path('book.html', views.book_view, name='book'),
    path('germany.html', views.germany_view, name='germany'),
    path('aust.html', views.aust_view, name='aust'),
]
