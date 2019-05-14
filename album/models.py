from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30)
    def save_category(self):
        self.save()



    def __str__(self):
        return self.category

class Location(models.Model):
    location=models.CharField(max_length=30)
    def save_location(self):
        self.save()


    def __str__(self):
        return self.location


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', blank = True)
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=30)
    location=models.ForeignKey(Location)
    category=models.ForeignKey(Category)

    '''function to save'''
    def save_image(self):
        self.save()

    '''function to delete'''
    def delete_image(self):
        to_delete=Image.objects.all()
        to_delete.delete()

    '''function to display'''
    @classmethod
    def display_images(cls):
        all_images=cls.objects.all()
        return all_images

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']
