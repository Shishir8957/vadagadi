from django.shortcuts import render
from .models import privacyPolicy
# Create your views here.
def privacy_policy(request):
    privacy = privacyPolicy.objects.all()
    return render(request, 'privacy_policy.html',{'privacy': privacy})