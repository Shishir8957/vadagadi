from django.shortcuts import render
from products.models import Product,PaymentComplete
from products.recommendation import get_recommendation
import random

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        if PaymentComplete.objects.filter(user=request.user).exists():
            k = PaymentComplete.objects.filter(user=request.user)
            j = random.sample(range(len(k)),1)
            if j[0] == 0:
                j[0]=1
            random_product = Product.objects.get(id__in=j)
            values= get_recommendation(random_product.name)
            suggestions=[]
            for i in range(8):
                if not Product.objects.get(id=values[i+1][1]).booked:
                    suggestions.append(Product.objects.get(id=values[i+1][1]))
            return render(request,'home.html',{'products':suggestions})
    product_count = Product.objects.all().order_by('rating').count()
    rand_entities = random.sample(range(product_count), 8)
    product = Product.objects.filter(id__in=rand_entities).filter(booked=False).order_by('rating')
    return render(request,'home.html',{'products':product})