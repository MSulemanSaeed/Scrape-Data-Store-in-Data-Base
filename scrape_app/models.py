from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    image = models.URLField(max_length=1000)

    def __str__(self) -> str:
        return self.title

