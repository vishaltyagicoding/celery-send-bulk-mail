import time
from django.shortcuts import render
from .models import All_Mail
from .tasks import send_welcome_email

def home(request):
    return render(request, 'emailer/home.html')
def send_bulk_emails(request):
    recipients = All_Mail.objects.all()
    for emails in recipients:
        send_welcome_email.delay(emails.email, emails.name)

    return render(request, 'emailer/success.html', {'count': len(recipients)})