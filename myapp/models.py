from django.db import models

class Link(models.Model):
    title = models.CharField(max_length=200)  # A title for the link
    url = models.URLField()  # The actual link

    def __str__(self):
        return self.title
