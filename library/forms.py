from django import forms
from .models import BookSuggestion, BookInquiry

INQUIRY_TYPE_CHOICES = [
    ('buy', 'I want to buy this book'),
    ('exchange', 'I want to exchange a book'),
    ('info', 'I want more information'),
]

class BookInquiryForm(forms.ModelForm):
    class Meta:
        model = BookInquiry
        fields = ['name', 'email', 'inquiry_type', 'message']
        labels={
            'name': 'Your name',
            'email': 'Your name',
            'inquiry_type': 'What you like to do?',
            'message': 'Message',
        }

        widgets = {
            'name': forms.TextInput(attrs={"placeholder": "Enter your full name"}),
            'email': forms.EmailInput(attrs={"placeholder": "email@example.com"}),
            'inquiry_type': forms.RadioSelect(choices=INQUIRY_TYPE_CHOICES),
            'message': forms.Textarea(attrs={"rows": 4, "placeholder": "Add any details or questions about this book"}),
        }



class BookSuggestionForm(forms.ModelForm):
    class Meta:
        model = BookSuggestion
        fields = ['name', 'email', 'suggested_title', 'suggested_author', 'message' ]
        labels = {
            'name':'Your name',
            'email' : 'Your email',
            'suggested_title' : 'Book title',
            'suggested_author' : 'Author (Optional)',
            'message' : 'Why are you suggesting this book?',
        }

        widgets = {
          'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
          'email': forms.EmailInput(attrs={'placeholder': 'you@email.com'}),
          'suggested_title': forms.TextInput(attrs={'placeholder': 'e.g. Sapiens, Clean Code, etc.'}),
          'suggested_author': forms.TextInput(attrs={'placeholder': 'Optional – e.g. Haruki Murakami'}),
          'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us why this book should be added'}),

        }




