from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    product = Product.objects.all().order_by('-id')[:10]
    return render(request, 'productpage.html',{'products':product})

def viewProduct(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'viewproduct.html',{'products':product})