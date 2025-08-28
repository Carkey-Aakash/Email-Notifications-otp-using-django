from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import random
from django.core.mail import send_mail

def index(request):
    return render(request,"index.html")

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken enter another.")
                return redirect('register')  

            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already taken: ")
                return redirect('register')  

            else:
                request.session['registration_data'] = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'username': username,
                    'password': password1,
                    'email': email,
                }
                
                otp= str(random.randint(100000,999999))
                request.session['email']=email
                request.session['otp']=otp

                send_mail(
                    subject='Otp verification for your account',
                    message=(f"Your otp is {otp}"),
                    from_email='carkeyaakash360@gmail.com',
                    recipient_list=[email],
                    fail_silently=False
                )


                messages.info(request, "OTP has been send to your email ")
                return redirect('verify_otp')  
        else:
            messages.error(request, "unmatched password")
            return redirect('register')  

    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username, password= password)

        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.error(request, "Access denied please login first")
                return redirect('login')
        else:
            messages.error(request, "Invalid username and password")
            return redirect('login')


    return render (request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def verify_otp(request):
    if not request.session.get('otp') or not request.session.get('registration_data'):
        messages.error(request,"Access Denied: register first")
        return redirect('register')
        
    if request.method=='POST':
        user_otp=request.POST['otp']
        session_otp=request.session.get('otp')
        

        if user_otp == session_otp:
            
            reg_data = request.session.get('registration_data')

            #  Create the user now, after OTP verification
            
            user = User.objects.create_user(
                username=reg_data['username'], first_name=reg_data['first_name'], last_name=reg_data['last_name'],
                email=reg_data['email'], password=reg_data['password'], is_active=True
            )
            user.save()
            messages.success(request, "your account has been verified:")

            request.session.pop('otp',None)
            request.session.pop('email', None)
            return redirect('login')
        else:
            messages.error(request,"Invalid Otp number")
            return redirect('verify_otp')
    else:
         return render (request, "verify_otp.html")

    