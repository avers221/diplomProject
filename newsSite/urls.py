from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('newsFeed.urls', namespace='newsFeed')),
    path('about_company/', include('about_company.urls', namespace='about_company'))
]