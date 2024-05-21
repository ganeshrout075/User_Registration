from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def register(request):
    EUFO = UserForm()
    EPFO = ProfileForm()
    d = {'EUFO': EUFO, 'EPFO':EPFO}
    if request.method == 'POST' and request.FILES:
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST, request.FILES)
        if UFDO.is_valid() and PFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            message=f"HEllo{UFDO.cleaned_data.get('first_name')}   message will sent successfully to our email id /n/n"
            email=UFDO.cleaned_data.get('email')
            send_mail(
                'Registration Successfully',
                message,
                "ganeshrout075@gmail.com",
                [email],
                fail_silently=False

            )
            return HttpResponse('registration is Done')
        return HttpResponse('Invalid Data')
    return render(request, 'register.html', d)
            
            
            # message=f"HEllo{UFDO.cleaned_data.get('first_name')}Your message will sent successfully"
            # email=UFDO.cleaned_data.get('email')
            # send_mail(
            #     'Registration Successfully',
            #     message,
            #     "ganeshrout075@gmail.com",
            #     [email],
            #     fail_silently=False

            # )
        