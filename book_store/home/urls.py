from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('library',views.lib,name='library'),
    path('<slug:c_slug>/', views.home,name='prod_cat'),
    path('search',views.searching,name='search'),
    path('<int:id>',views.detail,name='detail')
]
