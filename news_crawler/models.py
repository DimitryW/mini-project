from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255)
    paragraph = models.TextField()
    content = models.TextField()
    source = models.CharField(max_length=255, blank=True)
    news_url = models.URLField(unique=True)
    image_url = models.URLField(unique=True)
    image = models.ImageField(upload_to="news_images/", blank=True, null=True)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
