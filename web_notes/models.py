from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Additional information
# Django API, making queries https://docs.djangoproject.com/en/4.1/topics/db/queries/
# possible types of fields https://docs.djangoproject.com/en/4.1/ref/models/fields/


class Topic(models.Model):
    """Topics of notes to save in DB"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        """return text"""
        return self.text

class Note(models.Model):
    """Notes"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'notes'

    def __str__(self):
        """return string value"""
        if len(self.text) <= 50:
            return self.text
        else:
            return f"{self.text[:50]}..." #return the firts 50 symbols
    