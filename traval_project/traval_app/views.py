from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from.models import traval_table
from.models import team_table
# Create your views here.
def traval_fun(request):
    obj=traval_table.objects.all()
    team = team_table.objects.all()
    return render(request,'index.html',{'result':obj,'teams':team})
#REGISTRATION
def register_fun(request):
    if request.method == 'POST':
        u_name = request.POST['user_name']
        f_name = request.POST['first_name']
        l_name=request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        if password == re_password:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,"User Name Already Exists")
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('/register')
            else:
                user = User.objects.create_user(password=password,username=u_name,first_name=f_name,last_name=l_name,email=email)
                user.save()
                return redirect('/login')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('/register')
        return redirect('/index')
    return render(request, 'register.html')
#LOGIN
def login_fun(request):
    if request.method == 'POST':
        u_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=u_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request , "INVALID CREDENTIALS")
            return redirect('/login')
    return render(request, 'login.html')
#LOGOUT
def logout_fun(request):
    auth.logout(request)
    return redirect('/')
    #return render(request, 'index.html')