from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

CITY_NAME = (
    ('TORONTO','Toronto'),
    ('VANCOUVER', 'Vancouver'),
    ('CALGARY','Calgary'),
    ('MONTREAL','Montreal'),
    ('HALIFAX','Halifax'),
    ('WHITEHORSE','WhiteHorse'),
    ('WINNIPEG','Winnipeg'),
    ('QUEBEC CITY','Quebec City'),
    ('OTTAWA','Ottawa'),
)

class ImageInfo(models.Model):
    name = models.CharField(max_length=200, default="new image")
    location = models.CharField(max_length=200, choices=CITY_NAME, default='Toronto')
    category = models.CharField(max_length=200, default='travel')
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'images_id': self.id})



class Photo(models.Model):
    img_name = models.CharField(max_length=100, null=False, blank=False, default='image')
    url = models.CharField(max_length=200)
    image = models.ForeignKey(ImageInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for images_id: {self.image_id} @{self.url}"
