from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mountain
from blogapp.models import Profile
from django.contrib.auth.models import User
import collections

def add_mountain(request): #산 추가 기능
    if request.method == "GET":
        mountains = Mountain.objects.all()
        return render(request, 'add_mountain.html', {'mountains':mountains})

    elif request.method== "POST":
        mountain = Mountain()
        mountain.name = request.POST['mountain_name']
        mountain.address = request.POST['mountain_address']
        mountain.image = request.FILES['mountain_image']
        mountain.latitude = reqeust.POST['mountain_latitude']
        mountain.longtitude = request.POST['mountain_longtitude']
        mountain.save()
        return redirect(add_mountain)

def search_mountain(request):
    schText=request.GET['search']
    mountains = Mountain.objects.filter(name__icontains=schText)
    return render(request, 'search_mountain.html', {'mountains':mountains})

def complete_climbing(request, user): # 완등 페이지
    if request.method=="GET":
        mountains = Mountain.objects.all() # 산 정보 다 가져옴
        profile = Profile.objects.get(user= request.user) # 프로필 정보 가져옴
        count = request.user.complited.all() # request.user의 완등산 개수 확인을 위함
        context={
            "mountains" : mountains,
            "profile" : profile,
            "count" : count
            }
        return render(request, 'complete_climbing.html', context)

    elif request.method=="POST":
        mountain = Mountain.objects.get(name = request.POST['mt.name'])
        user = request.user
        if mountain.completed.filter(id = user.id).exists():
            mountain.completed.remove(request.user) #프로필의 완등한 산 추가
            mountain.completed_count -=1 #프로필의 완등한 수 ++
            mountain.save()
        else:
            mountain.completed.add(request.user) #프로필의 완등한 산 추가
            mountain.completed_count +=1 #프로필의 완등한 수 ++
            mountain.save() 
        return redirect('/mountainapp/complete_climbing/' + str(user))





