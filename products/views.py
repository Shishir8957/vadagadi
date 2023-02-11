from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.
def home(request):
  product = Product.objects.all().filter(booked=False).order_by('price').values()
  paginator = Paginator(product, 12)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'productpage.html',{'products':page_obj})

def payment(request):
  return render(request, 'payment.html')

@login_required(login_url='/register/')
def history(request):
    user = request.user
    if user.is_superuser:
      booking = Booking.objects.all()
    else:
      booking = Booking.objects.filter(name=user)
    return render(request,'history.html',{'history':booking})

def viewProduct(request,id):
  product = Product.objects.get(id=id)
  booking = Booking.objects.all()
  for i in booking :
    if product.id == i.product.id :
      booking = Booking.objects.get(id=i.id)
      print(booking)
      print(i.product.id)
      comments = Comment.objects.filter(product=product).order_by('-timestamp')
      return render(request, 'viewproduct.html',{'products':product,'comments':comments,'booking':booking})
  comments = Comment.objects.filter(product=product).order_by('-timestamp')
  return render(request, 'viewproduct.html',{'products':product,'comments':comments})

def car(request):
  data = Product.objects.filter(vehicleType='car')
  search = "Car's"
  return render(request, 'search.html',{'products':data,'search':search})

def price(request):
  product = Product.objects.all().filter(booked=False).order_by('-price').values()
  paginator = Paginator(product, 12)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'productpage.html',{'products':page_obj})

def name(request):
  product = Product.objects.all().filter(booked=False).order_by('name').values()
  paginator = Paginator(product, 12)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, 'productpage.html',{'products':page_obj})

def bike(request):
  data = Product.objects.filter(vehicleType='bike')
  search = "Bike's"
  return render(request, 'search.html',{'products':data,'search':search})

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
        
    return redirect(history)

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

@login_required(login_url='/register')
def postComment(request):
  if request.method == 'POST':
    comment = request.POST.get('comment')
    user = request.user
    postSno = request.POST.get('postSno')
    post = Product.objects.get(id=postSno)
    parentSno = request.POST.get("parentSno")
    if parentSno == "":
      comment = Comment(comment=comment,user=user,product=post)
    else:
      parent = Comment.objects.get(sno=parentSno) 
      comment = Comment(comment=comment,user=user,post=post,parent=parent)
    comment.save()
    # messages.success(request,"comment posted successfully")
  return redirect(f"/product/productdetail/{postSno}/")

@login_required(login_url='/register')
def deleteComment(request,slug):
  post = Comment.objects.filter(sno=slug)
  for posts in post:
    if posts.product.id != '':
      posts = posts.product.id
  print1=Comment.objects.filter(sno=slug)
  for p in print1:
    if request.user.username == p.user.username:
      Comment.objects.filter(sno=slug).delete()
      return redirect(f"/product/productdetail/{p.product.id}/")
  return redirect(f"/product/")