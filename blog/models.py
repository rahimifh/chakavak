from django.db import models
from django.utils import timezone
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:news_detail',
                    args=[self.publish.year,
                        self.publish.month,
                        self.publish.day, self.slug])
