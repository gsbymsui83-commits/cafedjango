from django.shortcuts import render

def goods_list(request):
    return render(request, 'goods/goods_list.html')