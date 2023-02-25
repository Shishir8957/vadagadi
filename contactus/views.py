from django.shortcuts import render
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import *

# Create your views here.
def contactus(request):
    return render(request,'contact.html')

def contactForm(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        message = request.POST.get('message')
        
        contact = Contact(name=name,email=email,contact_number=contact_number,message=message)
        contact.save()
        data={
            'name': name,
            'email': email,
            'contact_number': contact_number,
            'message': message, 
        }
        message= '''
            New message: {}

            Form: {}
        '''.format(data['message'],data['email'])

        send_mail('test email', message, 'royell4912@gmail.com', ['kbro1415@gmail.com'])
        return HttpResponse('<div style="text-align: center; margin: 17rem;">your form submitted <br> <a href="/" style="margin:1rem;" type="submit"> Return to home </a></div>')
    else:
        return render(request, 'contact.html')