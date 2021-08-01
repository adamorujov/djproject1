from django.shortcuts import render, redirect
from blog.forms import MailForm
from django.core.mail import send_mail

def send_maill(request):
    form = MailForm()
    if request.method == 'POST':
        form = MailForm(request.POST)

        if form.is_valid():
            sender = request.user.email
            subject = form.cleaned_data['subject']
            mail = form.cleaned_data['mail']
            recipients = [form.cleaned_data['receiver']]

            send_mail(sender, subject, mail, recipients, fail_silently=False)
            return redirect('mesajiletildi')
    
    context = {
        'form' : form,
    }

    return render(request, 'pages/send-mail.html', context)


