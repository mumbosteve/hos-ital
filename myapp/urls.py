
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('collection/',views.collection,name='collection'),
    path('inner-page/',views.innerpage,name='innerpage'),



]
