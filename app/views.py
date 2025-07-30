from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def portfolio(request):
    if request.method=='POST':
        un=request.POST['un']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['sub']
        msg=request.POST['msg']
        send_mail(subject,f'From {un} \n {msg} \n contact us: \n email:\n {email} \n Mobile: \n {phone}','thadesailaja@gmail.com',['thadesailaja@gmail.com'],fail_silently=False)
    return render(request,'home.html')