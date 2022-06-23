from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

from .models import Contact
# Create your views here.

def inquiry(request):

    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        contact_no = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)

            if has_contacted:
                messages.info(request, "You have already enquired about this car, please wait until we get back to you.")
                return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, 
                        city=city, state=state, email=email, contact_no=contact_no, message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        # send_otp_via_email(admin_email, car_title)
        # send_mail(
        #     'Car enquiry',
        #     'You have new enquiry for car ' + car_title + '. please login to check more info on enquiry.',
        #     'kirandjango9@gmail.com',
        #     [admin_email],
        #     fail_silently=False,
        # )

        contact.save()
        messages.success(request, 'Your request has been submitted, you will soon hear from us shortly')
        return redirect('/cars/'+car_id)

    return render(request, 'accounts/inquiry.html')


def send_otp_via_email(email, car_title):
    subject = "Carzone : Car enquiry"
    message = 'You have new enquiry for car ' + car_title + '. please login to check more info on enquiry.',
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    