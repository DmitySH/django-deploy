from django.db import models
from django.contrib.auth.models import User
from pytils.translit import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    is_verified = models.BooleanField(default=False)
    news_count = models.IntegerField(default=0, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL",
                            default=None, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(default='', verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

