from django.db import models
from django.urls import reverse

# Create your models here.

CITY_CHOICES = (
    ('AUS', 'Austin'),
    ('SMA', 'Santa Monica'),
    ('DAL', 'Dallas'),
)

class Meme(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=250)
    image_upload = models.ImageField(
        upload_to='images/',
        default='../RickRoll.jpg')
    description = models.TextField(max_length=250)
    date = models.DateField('creation date')
    city = models.CharField(
        max_length = 3,
        choices = CITY_CHOICES,
        default = CITY_CHOICES[0][0]
    )
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def __str__(self):
        return f"{self.get_city_display()} on {self.author}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'meme_id: self.id'})

class History(models.Model):
    contribution_text = models.TextField(max_length=250)
    contribution_date = models.DateField('contribution date')
    contribution_image = models.ImageField(
        upload_to='images/',
        default='../RickRoll.jpg')
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.contribution_text} on {self.contribution_date}"
    
