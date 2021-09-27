from django.db import models

# Create your models here.
class Adventure(models.Model):
    adventurename = models.CharField(max_length=200)
    adventuretext = models.CharField(max_length=2000, null=True)
    photo_url = models.TextField()
    def __str__(self):
        return self.adventurename

class Path(models.Model):
    adventure = models.ForeignKey(
        Adventure,
        on_delete=models.CASCADE,
        related_name="paths"
    )
    pathname = models.CharField(max_length=200, default="there is no path")
    pathtext = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.pathname

class RouteTableOne(models.Model):
    path = models.ForeignKey(
        Path,
        on_delete=models.CASCADE,
        related_name="routetableone"
    )

    routename = models.CharField(max_length=200, default="there is no path")
    routetext = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.routename

class RouteTableTwo(models.Model):
    path = models.ForeignKey(
        Path,
        on_delete=models.CASCADE,
        related_name="routetabletwo"
    )
    
    routename = models.CharField(max_length=200, default="there is no path")
    routetext = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.routename

class RouteTableThree(models.Model):
    path = models.ForeignKey(
        Path,
        on_delete=models.CASCADE,
        related_name="routetablethree"
    )
    routename = models.CharField(max_length=200, default="there is no path")
    routetext = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.routename

class GoodEnding(models.Model):
    goodending = models.ForeignKey(
        RouteTableOne,
        on_delete=models.CASCADE,
        related_name="goodending"
    )
    endingname = models.CharField(max_length=200, default="there is no ending")
    endingtext = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.endingname

class BadEnding(models.Model):
    badending = models.ForeignKey(
    RouteTableTwo,
    on_delete=models.CASCADE,
    related_name="badending"
    )
    endingname = models.CharField(max_length=200, default="there is no ending")
    endingtext = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.endingname

class NeutralEnding(models.Model):
    neutralending = models.ForeignKey(
    RouteTableThree,
    on_delete=models.CASCADE,
    related_name="neutralending"
    )
    endingname = models.CharField(max_length=200, default="there is no ending")
    endingtext = models.CharField(max_length=100, default="no path text")
    photo_url = models.TextField(max_length=2000, null=True)
    def __str__(self):
        return self.endingname

