from allauth.account.utils import sync_user_email_addresses
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class UserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='static/images/avatars', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:userprofile-detail',
                       kwargs={'id': self.id}
                       )


class Category(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Article(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    OPTIONS = (
        ('draft', 'draft'),
        ('published', 'published')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    titre = models.CharField(max_length=100)
    excerpt = models.TextField(null=True)
    image = models.ImageField(upload_to='static/images/article', blank=True, null=True)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique_for_date='published', null=True)
    author = models.ForeignKey(UserProfile, on_delete=models.PROTECT, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=OPTIONS, default='draft')

    def __str__(self):
        return self.titre



def user_receiver(sender, instance, created, *args, **kwargs):

    if created:
        sync_user_email_addresses(instance)

post_save.connect(user_receiver, sender=UserProfile)