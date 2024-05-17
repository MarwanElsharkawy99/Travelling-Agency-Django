from django.db import models


class package(models.Model):
    name=models.CharField(max_length=256)
    price=models.FloatField(max_length=256)
    description=models.TextField()
    dest_from=models.CharField(max_length=256)
    dest_to=models.CharField(max_length=256)
    img=models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.name
    
class blog(models.Model):
    blog_title=models.CharField(max_length=250)
    blog_writer=models.CharField(max_length=250)
    blog_content=models.TextField()
    img=models.ImageField(upload_to='media')
    time=models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.blog_title
    
    
    
