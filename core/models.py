from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=15)
    introduction = models.TextField()
    subtitle1 = models.CharField(max_length=200, blank=True, null=True)
    paragraphe1 = models.TextField(blank=True, null=True)
    subtitle2 = models.CharField(max_length=200, blank=True, null=True)
    paragraphe2 = models.TextField(blank=True, null=True)
    subtitle3 = models.CharField(max_length=200, blank=True, null=True)
    paragraphe3 = models.TextField(blank=True, null=True)
    subtitle4 = models.CharField(max_length=200, blank=True, null=True)
    paragraphe4 = models.TextField(blank=True, null=True)
    subtitle5 = models.CharField(max_length=200, blank=True, null=True)
    paragraphe5 = models.TextField(blank=True, null=True)
    subtitle6 = models.CharField(max_length=200, blank=True, null=True)
    paragraphe6 = models.TextField(blank=True, null=True)
    conclusion = models.TextField()

    def __str__(self):
        return self.title
    