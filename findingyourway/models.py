from django.db import models

# Create your models here.
class Adventure(models.Model):
    adventure = models.CharField(max_length=200)
    adventuretext = models.CharField(max_length=2000, null=True)
    photo_url = models.TextField()
    def __str__(self):
        return self.adventure

class Path(models.Model):
    adventure = models.ForeignKey(
        Adventure,
        on_delete=models.CASCADE,
        related_name="adventures"
    )
    path = models.CharField(max_length=200, default="there is no path")
    pathtext = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.path