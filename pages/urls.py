from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('intro/', views.intro_page, name='intro_page'),
    path('location/', views.location_page, name='location_page'),
]
