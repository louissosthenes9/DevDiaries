from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status='published')
# Create your models here.
class Post(models.Model):
     #enum class for the status model
    class Status(models.TextChoices):
        DRAFT = 'DF'
        PUBLISHED = 'PB'

    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLISHED)

    objects = models.Manager()
    published = PublishedManager()
    class Meta:
        ordering = ['-pub_date']
        indexes = [models.Index(fields=['-pub_date'])]


    def __str__(self):
        return self.title
