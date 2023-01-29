import email
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import secrets
import string
    
def error404(request):
    return render(request,'404.html')

@login_required(login_url='/register')
def userprofile(request):
    user = request.user
    return render(request,'user-profile.html')

@login_required(login_url='/register')
def userprofileUpdate(request,id):
    if request.method == 'POST':
        img = request.POST['img']
        print('image',type(img))
    user = request.user
    return render(request,'user-profile.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register') 
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')     
            else:    
                token = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7))
                send_mail('Register your email', f"Register your email http://20.40.54.252/register/activateUser/{token}/ ", 'royell4912@gmail.com', [email],fail_silently=False)
                user = User.objects.create_user(username=username,first_name=first_name,email=email,password=password1)
                user.is_active=False
                user.save(); 
                randomString.objects.create(random=token,user=user).save
                messages.info(request,'Please Check Your Email for verification')
                return render(request,'account.html',{'color':True})
        else:
            messages.info(request,'password does not match')
            return redirect('/register')   
    else:    
        return render(request,'account.html')

def activateUser(request,slug):
    for token in randomString.objects.filter(random=slug):
        if (token.random == slug) or (token.user.is_active == True):
            user = token.user
            user.is_active=True
            user.save();
            randomString.objects.filter(random=slug).delete()
            messages.info(request,'Enter your credientials')
            return redirect('register')
    else:
        messages.info(request,'link no longer valid')
    return redirect('register')

def login(request):        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')   
    else:    
        return render(request,'account.html')
        
def logout(request):
    auth.logout(request)
    if request.method == 'POST':
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
    return redirect('register')

def password_reset(request):
    return render(request,'password_reset.html')

def email_submited(request):
    if request.method == 'POST':
        email = request.POST['email']
        token = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7))
        u=User.objects.filter(email=email)
        if not u:
            send_mail('Register your email', f"Register your email http://20.40.54.252/register/ ", 'royell4912@gmail.com', [email],fail_silently=False)
        else:
            for user in u:
                token = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7))
                send_mail('Reset password', f"Reset password http://20.40.54.252/register/password_reset/{token}/ ", 'royell4912@gmail.com', [email],fail_silently=False)
                print(user)
                randomString.objects.create(random=token,user=user).save
    return HttpResponse('<div style="text-align: center; margin: 17rem;">Please check your email<br> <a href="/blog" style="margin:1rem;" type="submit"> Return to home </a></div>')

def userValid(request,slug):
    for token in randomString.objects.filter(random=slug):
        if (token.random == slug):
            return render(request,'new_password.html') 
    else:
        messages.info(request,'link no longer valid')
        return redirect('login')

def update_password(request,slug):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            users = randomString.objects.filter(random=slug)
            for user in users:
                username = user.user.username
                email = user.user.email
                user = User.objects.get(username=user.user)
                user.set_password(password1)
                user.save(); 
                send_mail('Your password change successfully', f"Your password change successfully for {username} ", 'royell4912@gmail.com', [email],fail_silently=False)
                randomString.objects.filter(random=slug).delete()
            messages.info(request,'Password Updated Successfully')
            return redirect('register')
        else:
            messages.info(request,'password does not match')
            return redirect(f'/register/password_reset/{slug}') 
    return redirect('register')

def search(request): 
    return render(request,'index.html')