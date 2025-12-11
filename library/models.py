from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    available = models.BooleanField(default=True)

    cover_image = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class BookSuggestion(models.Model):
    SUGGESTION_STATUS_CHOICES = [
        ('new', 'New'),
        ('reviewed','Reviewed'),
        ('rejected','Rejected'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    suggested_title = models.CharField(max_length=200)
    suggested_author = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices = SUGGESTION_STATUS_CHOICES,
        default = 'new',
    )

    created_at = models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        if self.suggested_author:
            return f"{self.suggested_title} by {self.suggested_author} (suggested by {self.name})"
        return f"{self.suggested_title} (suggested by {self.name})"


class BookInquiry(models.Model):
    INQUIRY_TYPE_CHOICES=[
        ('buy','I want to buy this book'),
        ('exchange', 'I want to exchange a book' ),
        ('info', 'I want more information'),
    ]

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='inquiries'
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.book.title} by {self.name}"