from django.db import models
from django.urls import reverse


# Create your models here.

class info(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pictures')
    dis= models.TextField()
    cont= models.FileField()


    def get_absolute_url(self):
        return reverse("mt",kwargs={"id":self.id})