"""DrfOauthMongodb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from users.models import User
from DrfOauthMongodb.api import CustomTokenView
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('houses/', include('houses.urls')),
    path('drf/', include('drf_house_test.urls')),
    path('pymongo/', include('pymongo_db_control.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('o/customtoken/', CustomTokenView.as_view(), name='token_obtain_pair'),
]
