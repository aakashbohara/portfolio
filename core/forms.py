"""
Portfolio Forms
"""

from django import forms
from .models import ContactMessage, NewsletterSubscriber


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message', 'budget', 'project_type']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Email',
                'required': True
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Subject',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Your Message',
                'rows': 5,
                'required': True
            }),
            'budget': forms.Select(attrs={
                'class': 'form-input'
            }, choices=[
                ('', 'Select Budget (Optional)'),
                ('< $1,000', 'Less than $1,000'),
                ('$1,000 - $5,000', '$1,000 - $5,000'),
                ('$5,000 - $10,000', '$5,000 - $10,000'),
                ('$10,000+', '$10,000+'),
            ]),
            'project_type': forms.Select(attrs={
                'class': 'form-input'
            }, choices=[
                ('', 'Project Type (Optional)'),
                ('Web Development', 'Web Development'),
                ('Mobile App', 'Mobile App'),
                ('UI/UX Design', 'UI/UX Design'),
                ('Consulting', 'Consulting'),
                ('Other', 'Other'),
            ]),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your email',
                'required': True
            }),
        }
