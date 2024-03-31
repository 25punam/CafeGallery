from django.shortcuts import render
from django.db.models import Q
from cafe.models import MenuModel, CafeModel

# Create your views here.

def menu(request, cafe_id):
    context = {}
    cafe_obj = CafeModel.objects.get(id = cafe_id)
    context ['cafe'] = cafe_obj

    eat_menu = MenuModel.objects.filter(Q(type = 'Eat') & Q(cafe = cafe_id))
    context ['eat'] = eat_menu

    drink_menu = MenuModel.objects.filter(Q(type = 'Drink') & Q(cafe = cafe_id))
    context ['drink']= drink_menu

    # img_obj = MenuModel.objects.get(id=4)
    # context ['image'] = img_obj
    return render(request,'menu.html',context)

def home(request):
    context = {}
    cafe = CafeModel.objects.all() # filter / all / exclude -> Iterate
    context['cafe_obj'] = cafe
    return render(request,'home.html',context)



