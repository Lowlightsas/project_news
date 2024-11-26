from django.db import models
from django.utils import timezone 
from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    
    category_name = models.CharField(max_length=255)
    category_slug = models.SlugField(max_length=255,unique=True)
    
    class Meta:
        ordering = ['category_name']
        indexes = [models.Index(fields=['category_name']),]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name
     
    def get_absolute_url(self):
        return reverse('news:news_list_by_category',
                       args=[self.category_slug])
    
    
class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=News.Status.PUBLISHED)

class News(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        PUBLISHED = 'PB','Published'

    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='news_post')
    category = models.ForeignKey(Category,related_name='news',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    text = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['id','slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news:news_detail", args=[self.id])
    
    
class NewsAttachment(models.Model):

    news = models.ForeignKey(News, related_name='attachments', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="user/%Y/%m/%d/",blank=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.news.title}"
    
class Comment(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='author_comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['active']),
        ]
    def __str__(self):
        return f'Comment by {self.author} on {self.news}'