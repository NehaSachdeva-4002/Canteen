from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import canteen, Order
def home(request):
    Canteen = canteen.objects.all()
    return render(request, 'home.html', {'Canteen': Canteen})


def add_to_cart(request, item_id):
    item = get_object_or_404(canteen, id=item_id)
    Order.objects.create(item=item)
    return redirect('canteen-home')
