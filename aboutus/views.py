from django.shortcuts import render

# Create your views here.
def aboutus(request):
    return render(request,'aboutus.html')