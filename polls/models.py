from django.db import models

# Create your models here.

class NewsModel(models.Model):
    title = models.CharField(default=' ',max_length=120)
    body = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
    
