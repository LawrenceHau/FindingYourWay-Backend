from django.db import models

# Create your models here.
class Adventure(models.Model):
    adventure = models.CharField(max_length=200)
    text = models.CharField(max_length=2000, null=True)
    photo_url = models.TextField()
    def __str__(self):
        return self.adventure

class Path(models.Model):
    adventure = models.ForeignKey(
        Adventure,
        on_delete=models.CASCADE,
        related_name="paths"
    )
    path = models.CharField(max_length=200, default="there is no path")
    text = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.path

class Route(models.Model):
    path = models.ForeignKey(
        Path,
        on_delete=models.CASCADE,
        related_name="routes"
    )

    route = models.CharField(max_length=200, default="there is no path")
    text = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.route

class Ending(models.Model):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name="endings"
    )
    ending = models.CharField(max_length=200, default="there is no ending")
    text = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.ending
