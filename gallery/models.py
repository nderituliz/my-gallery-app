from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=255)
    image_location = models.ForeignKey('Location',on_delete=models.CASCADE)
    image_category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image= models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.image_name

    @classmethod
    def save_image(self):
        self.save()


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category