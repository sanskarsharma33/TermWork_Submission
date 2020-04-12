from django.shortcuts import render
from .models import UserDetails
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from . import forms
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json,io

# Create your views here.

def Login(request):
    c = {}
    c.update(csrf(request))
    return render(request,"logind.html",context=None)


def auth_view(request):
    usrname=request.POST.get("usr",'')
    passwd=request.POST.get("pass",'')
    user=authenticate(username=usrname,password=passwd)
    if user is not None:
        login(request, user)
        curr_user=UserDetails.objects.all().get(user = user)
        print(curr_user.first_name,curr_user.last_name,curr_user.email)
        if  curr_user.first_name != 'null' :
            print(curr_user.first_name,curr_user.last_name,curr_user.email)
            return(HttpResponse("OK"))
        else :
            return(redirect('/login/change_profile'))
    else:
        return(HttpResponse("Wrong Credentials"))

@login_required(login_url='/login/loginpage/')
@csrf_exempt
def change_profilepage(request):
    c = {}
    c.update(csrf(request))
    if request.method=="POST":
        try:
            user = UserDetails.objects.all().get(user=request.user)
        except UserDetails.DoesNotExist:
            return HttpResponse(status=404)
        data=request.POST.copy()
        data['user']=request.user.id
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
           serializer.save()
        else:
           return JsonResponse(serializer.errors, status=400)
        #return JsonResponse(serializer.data, status=201)
        return redirect('/login/change_password/')
    else:
        pform=forms.ProfileForm()
    return render(request,"createuser.html",{'pform': pform})


@login_required(login_url='/login/loginpage/')
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return HttpResponse("Successfully Changed!!")
        else:
            return HttpResponse("WRONG!")
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form' : form }
        return render(request,'change_password.html',args)

def Logout(request):
    logout(request)
    return redirect("/login/loginpage/")
