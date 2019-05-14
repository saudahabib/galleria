from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Location(models.Model):
    location=models.CharField(max_length=30)
    def __str__(self):
        return self.image_name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', blank = True)
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=30)
    location=models.ForeignKey(Location)
    category=models.ForeignKey(Category)

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']
