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