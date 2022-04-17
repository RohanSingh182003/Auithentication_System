from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

# Create your views here.
# username='Admin_User'
# password='$$$$test1234@user'
def index(request):
    if request.user.is_anonymous:
        return redirect('/loginuser')
    else:
        return render(request,'index.html')
    # redirect('/loginuser')

def loginuser(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            params = {'reject':'Wrong! Username / Password , Enter Correct One..'}
            return render(request,'login.html',params)
            
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/loginuser')

