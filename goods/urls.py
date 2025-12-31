from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('goods-list/', views.goods_list, name='goods_list'),
]
