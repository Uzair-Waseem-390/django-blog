from django.db import models

# Create your models here.

class AboutUs(models.Model):
    about_title = models.CharField(max_length=20)
    about_description = models.TextField(max_length=200)
    
    
    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
    
    def __str__(self):
        return self.about_title
    

class FollowUs(models.Model):
    platform_name = models.CharField(max_length=100)
    platform_url = models.URLField(max_length=500)
    
    
    class Meta:
        verbose_name = 'Follow Us'
        verbose_name_plural = 'Follow Us'
    
    def __str__(self):
        return self.platform_name