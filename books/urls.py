"""SellMyBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove'),
    path('dataentry', views.dataentry, name='dataentry'),
    path('emailentry', views.emailentry, name='emailentry'),
    path('product_page', views.product_page, name="product_page"),
    path('profile', views.myads, name="my ads"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
