from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('sih/',views.sih,name='sih'),
    path('travel_destination/',views.travel_destination,name='travel_destination'),
    path('destination_details/',views.destination_details,name='destination_details'),
    path('shnongpdeng/',views.shnongpdeng,name='shnongpdeng'),
]

