from django import forms

class ContactForm(forms.Form):
    COURSES = [
        ('minecraft', 'Minecraft'),
        ('python', 'Python'),
        ('scratch', 'Scratch'),
        ('html', 'HTML'),
        ('unity', 'Unity'),
    ]
    
    subject = forms.CharField(max_length=100, label='Тема листа')
    email = forms.EmailField(required=False, label='Ваша електронна адреса')
    course = forms.ChoiceField(choices=COURSES, label='Курс')
    message = forms.CharField(widget=forms.Textarea, label='Текст листа')
