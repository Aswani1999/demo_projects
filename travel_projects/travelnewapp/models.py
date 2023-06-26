from django.db import models


class work(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.name

class member(models.Model):
    names=models.CharField(max_length=200)
    images=models.ImageField(upload_to='picture')
    des=models.TextField()

    def __str__(self):
        return self.names

