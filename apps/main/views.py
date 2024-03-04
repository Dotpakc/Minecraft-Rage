from django.core.mail import send_mail

from django.shortcuts import render
#messages
from django.contrib import messages

from .forms import ContactForm

# Create your views here.
def index(request):
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'core/index.html', context)


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            course = form.cleaned_data['course']
            message = form.cleaned_data['message']
            
            text = f'Ви вибрали курс: {course}\n\n{message}\\n\nВаша електронна адреса: {email}'
            
            send_mail(subject, text, 'noreply@robosmart.pp.ua', [f'{email}'])
            messages.success(request, 'Лист відправлено')
            return render(request, 'core/index.html')
        else:
            messages.error(request, 'Помилка відправлення листа')
    else:
        form = ContactForm()
    return render(request, 'core/index.html', {'form': form})