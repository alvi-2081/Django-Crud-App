
from django.urls import include
from django.urls import path
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('firstapp/', include('firstapp.urls')),
    path('app1/', include('app1.urls')),
    path('admin/', admin.site.urls),

    path('admin/', admin.site.urls),
    path('api/v1/todo/', include("app1.urls"))
]
