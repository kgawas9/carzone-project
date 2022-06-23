from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('dashboard')

        else:
            messages.error(request, 'incorrect username and password..')
            return redirect('login')
            
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
    return redirect('homePage')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Password does not matched')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, f'Username {username} already exist')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, f'Your email {email} already exist')
            return redirect('register')

        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password
        )
        user.save()
        auth.login(request,user)
        messages.success(request, 'you are logged in to the website')
        return redirect('dashboard')

    return render(request, 'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    user_enquiry_queryset = Contact.objects.filter(user_id=request.user.id).order_by('-created_date')
    context = {
        'enquiry': user_enquiry_queryset,
    }
    return render(request, 'accounts/dashboard.html', context=context)