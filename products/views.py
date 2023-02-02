from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Booking
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    product = Product.objects.all().filter(booked=False)
    paginator = Paginator(product, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'productpage.html',{'products':page_obj})

def viewProduct(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'viewproduct.html',{'products':product})

@login_required(login_url='/register/')
def bookdate(request,pk):
    if request.method == "POST":
        starting = request.POST['starting']
        ending = request.POST['ending']
        pickuptime = request.POST['pickuptime']
        needDriver = request.POST.getlist('needDriver')
        starting = datetime.strptime(starting, "%b %d, %Y").date()
        ending = datetime.strptime(ending, "%b %d, %Y").date()

        if str(starting-ending) == '0:00:00':
            a = 0
        else:
            a= (str(starting-ending).split(" "))[0]
        time = datetime.strptime(pickuptime,'%I:%M %p').time()

        product = Product.objects.get(id=pk)
        user = request.user

        if len(needDriver):
            needDriver = True
        else:
            needDriver = False

        if Product.objects.get(id=pk).booked:
            print("product is already booked")
            return redirect('/')
        else:
            product.booked=True
            product.save()
            event = Booking.objects.create(name=user,starting=starting,ending=ending,pickupTime=time,total_days=a,cost_per_day=product.price,product=product,driverStatus=needDriver)
            event.save()
        
    return redirect('register')

def CancelOrder(request,pk):
    user = request.user
    if user.username == Booking.objects.get(product_id=pk).name:
        return redirect('register')
    return redirect('/')
    
def search(request):
  if 'search' in request.GET:
    global search 
    search = request.GET['search']
    print(search)
    data = Product.objects.filter(name__icontains=search)
    num=len(list(data))
    print(data)
  else:
    data = Product.objects.all()
  return render(request, 'search.html',{'products':data, 'search':search,'table':num})
