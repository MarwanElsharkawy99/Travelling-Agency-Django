from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Day(models.Model):
    package = models.ForeignKey(Package, related_name='days', on_delete=models.CASCADE)
    day_number = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"

class Activity(models.Model):
    day = models.ForeignKey(Day, related_name='activities', on_delete=models.CASCADE)
    time_of_day = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.time_of_day} - {self.description[:50]}"
