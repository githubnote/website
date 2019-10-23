from django.db import models

# Create your models here.

class site_info(models.Model):
    site_name = models.CharField(max_length=100)
    site_slogan = models.CharField(max_length=100)
    site_author = models.CharField(max_length=100)


    def __str__(self):
        return self.site_name
