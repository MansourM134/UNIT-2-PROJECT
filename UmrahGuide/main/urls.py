
from django.urls import path
from . import views
app_name = "main"

urlpatterns = [

    path("", views.home, name="home"),
    path('preparations/', views.preparations, name='preparations'),
    path('umrah_steps/', views.umrah_steps, name='umrah_steps'),
    path('general_info/', views.general_info, name='general_info'),
    path('map_locations/', views.map_locations, name='map_locations'),
    path('how_to_use/', views.map_locations, name='how_to_use'),


]
