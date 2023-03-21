from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from products.models import Booking,Product
from django.core.mail import send_mail

@login_required(login_url='/register/')
def history(request):
    user = request.user
    booking = Booking.objects.filter(name=user)
    return render(request,'history.html',{'history':booking})

@login_required(login_url='/register/')
def delete(request,id):
    user = request.user
    products = Product.objects.get(id=id)
    try:
        send_mail('Order Cancel', f"Vehicle Booking Order Cancel http://127.0.0.1:8000/product/productdetail/{id}/ ", 'royell4912@gmail.com', [request.user.email],fail_silently=False)
    except:
        print('Error sending mail')
    products.booked = False
    products.save()
    Booking.objects.get(product=products).delete()
    booking = Booking.objects.filter(name=user)
    return redirect('/product/history/')