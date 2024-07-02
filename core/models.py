from django.db import models


class package(models.Model):
    name=models.CharField(max_length=256)
    price=models.FloatField(max_length=256)
    description=models.TextField()

    dest_from=models.CharField(max_length=256)
    dest_to=models.CharField(max_length=256)
    img=models.ImageField(upload_to='media')
    Included=models.TextField(default="NO conditions")
    Excluded=models.TextField(default="NO conditions")
    def overview_lines(self):
        return filter(None, (line.strip() for line in self.Included.splitlines()))
    def overview_lines1(self):
        return filter(None, (line.strip() for line in self. Excluded.splitlines()))
    
    def __str__(self):
        return self.name
    
class gallery(models.Model):
    package = models.ForeignKey(package, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField()

   




class blog(models.Model):
    blog_title=models.CharField(max_length=250)
    blog_writer=models.CharField(max_length=250)
    blog_content=models.TextField()
    img=models.ImageField(upload_to='media')
    time=models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.blog_title
    
    
    
class Day(models.Model):
    package = models.ForeignKey(package, related_name='day', on_delete=models.CASCADE)
    day_number = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"
    

class Hotel(models.Model):
 
    package = models.ForeignKey(package, related_name='hotel', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    star_rating = models.IntegerField()
    website = models.URLField()
    img=models.ImageField(upload_to='media',default="null")

    def __str__(self):
        return f"{self.name} ({self.city})"