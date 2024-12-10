from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages 

# Create your views here.

def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    
    if request.method == "POST":  
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')
   
        message = f"""
                <div style="display: flex; justify-content: start; align-items: center; padding: 8px;">
                    <div style="padding: 16px; width: fit-content;">
                        <div style="text-align: start;">
                            <p>{fullname}, {email}</p>
                            <p>{msg}</p>  
                        </div>
                        <div style="margin-top: 24px; text-align: start;">
                            <p>© 2023 Afrikbook™. All Rights Reserved.</p>
                            <p><a href="afrikbook.com" style="color: #007BFF;">Afrikbook.com</a></p>
                        </div>
                    </div>
                </div>
            """

        try:
            send = send_email(email, subject, message)
            
            messages.success(request, "Your message was sent, thank you!")
        except Exception as e:
            messages.success(request, e)
        
    # else:
    

    return render(request, "contact.html")

def mannual(reqest):
    return render(reqest, "mannual.html")






def send_email(email, title, message):
   
    email_to_send  = EmailMessage(
        subject=title, 
        body=message, 
        from_email=settings.EMAIL_HOST_USER, 
        to=[settings.EMAIL_HOST_USER], 
        reply_to=[email],
    )
    email_to_send.content_subtype = "html"
    result = email_to_send .send(fail_silently=False,)
    # if result == len(email):
    #     return True
    # else:
    #     return False
