from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def home(request):
    return render(request, "Medilab/home.html")

def services(request):
    return render(request, "Medilab/services.html")

def book_an_appointment(request):
    return render(request, "Medilab/book_an_appointment.html")

def nearby_hosp(request):
    return render(request, "Medilab/nearby_hosp.html")

def chat(request):
    return render(request, "Medilab/chat_with_us.html")

def contact(request):
    return render(request, "Medilab/contact.html")

def login(request):
    return render(request,"Medilab/login.html")

def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        mobile= request.POST['mobile']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
        user.save()
        print("user created")
        return redirect('/')
    else:
        return render(request,"Medilab/registration.html")

