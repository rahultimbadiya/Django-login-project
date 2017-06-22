from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import UserData
from django.contrib import messages

def index(request):
    context = {}
    return render(request,'index.html',context)

def home(request):
    context = {}
    return render(request,'home.html',context)

def login(request):

    if request.method == 'POST':
        u_name = request.POST['username']
        p_word= request.POST['password']

        try:
            my_uname = UserData.objects.get(Username=u_name)
            context = {
                'userdata': my_uname,
            }

            if my_uname.Password == p_word:
                return render(request,'home.html',context)
            else:
                messages.error(request,'Invalid Password,Please try again')
                return redirect('index')
        except:
            messages.error(request,'Invalid Username,Please try again')
            return redirect('index')


def signup(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        email = data['email']
        password = data['password']

        exist_user_list = UserData.objects.all().values_list('Username',flat=True)
        if username not in exist_user_list:
            store_data = UserData(Firstname=firstname,Lastname=lastname,Username=username,Email=email,Password=password)
            store_data.save()
            messages.success(request,'Created account Successfully, Please Log In to go to Home page')
            return redirect('index')
        else:
            messages.error(request,'Username already exist, Please try again')
            return render(request,'index.html',context)
    else:
        messages.error(request,'Data is not entered properly, Try again')
        return render(request,'index.html',context)







