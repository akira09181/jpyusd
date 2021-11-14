from django.urls import path

from . import views
app_name = 'tradeJpyUsd'
urlpatterns = [
    path('',views.index,name='index'),
    path('Sma',views.Sma,name='Sma'),
]