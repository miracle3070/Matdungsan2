from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import auth
import os,sys
# Create your views here.
def signup(request):
    if request.method == 'POST': #값이 넘겨졌을 경우 
        if request.POST['password1'] == request.POST['password2']:  # password 1,2입력된 값이 같다면
            # user 객체를 새로 생성
            user = User.objects.create_user(
                   username=request.POST['id'], password=request.POST['password1'], email=request.POST['email'])
            user.profile.name=request.POST['name']
            user.profile.nickname= request.POST['nickname']
            user.profile.gender=request.POST['gender']
            user.profile.age_group=request.POST['age_group']
            user.profile.grade = request.POST['grade']
            try:
                user.profile.image=request.FILES['image']
            except:
                pass
            auth.login(request, user)
            return redirect('/') #첫화면으로
    return render(request, 'signup.html') #아닌 경우는 그저 페이지 보여주기


def login(request):
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장하기.
        username = request.POST['id']
        password = request.POST['password']
        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        # 해당 user 객체가 존재한다면(객체가 존재하지 않는다면 none을 반환할 텐데, none이 not이니까 존재한다면!)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')



def logout(request):
    if request.method == 'POST':
         auth.logout(request)
         return redirect('/')
    return render(request, 'signup.html')    