from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # in this case if the user is deleted, all their topics go. May not be the best future practice
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """"Something specific about the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # just to prevent 'entrys'
        verbose_name_plural = 'entries'

    # info shown when refers to individual entries, clipped to 50 char
    def __str__(self):
        """return a string representation of the model"""
        if len(self.text) < 50:
          return f"{self.text}"
        else:
          return f"{self.text[:50]}..."