from django import forms

INQUIRY_TYPE_CHOICES = [
    ('buy', 'I want to buy this book'),
    ('exchange', 'I want to exchange a book'),
    ('info', 'I want more information'),
]

class BookInquiryForm(forms.Form):
    name = forms.CharField(
        label="Your name",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Enter your full name"})
    )
    email = forms.EmailField(
        label="Your email",
        widget=forms.EmailInput(attrs={"placeholder": "your@email.com"})
    )
    inquiry_type = forms.ChoiceField(
        label="What would you like to do?",
        choices=INQUIRY_TYPE_CHOICES,
        widget=forms.RadioSelect
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Add any details or questions about this book"})
    )
