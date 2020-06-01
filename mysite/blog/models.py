from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=10)
    #name = models.CharField(max_length=256)

    title=models.CharField(max_length=50)
    text =models.CharField(max_length=255, null = True, blank = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs = {'pk':self.pk})

class Comments(models.Model):
    author = models.CharField(max_length=10, null = True, blank = True)
    text =models.CharField(max_length=255, null = True, blank = True)
    #date_posted = models.DateTimeField(default = timezone.now)
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs = {'pk':self.pk})
