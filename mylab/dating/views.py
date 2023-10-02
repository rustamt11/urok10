from django.shortcuts import render
from dating.models import Person

# Create your views here.
def show_profiles(request):
    context = {'profiles': Person.objects.all()}
    return render(request,
                  'index.html',
                  context=context)
def show_profile(request, profile_id):
    context = {"profile": Person.objects.get(pk=profile_id)}
    return render(request,
                  "profile.html",
                  context=context)