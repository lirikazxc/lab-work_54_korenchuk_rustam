
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


import webapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("webapp.urls"))
]
