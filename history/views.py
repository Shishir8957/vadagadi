from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from products.models import Booking,Product

@login_required(login_url='/register/')
def history(request):
    user = request.user
    booking = Booking.objects.filter(name=user)
    return render(request,'history.html',{'history':booking})

@login_required(login_url='/register/')
def delete(request,id):
    user = request.user
    products = Product.objects.get(id=id)
    products.booked = False
    products.save()
    Booking.objects.get(product=products).delete()
    booking = Booking.objects.filter(name=user)
    return redirect('/product/history/')