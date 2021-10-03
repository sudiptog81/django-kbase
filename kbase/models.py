import string
import random

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from tinymce.models import HTMLField


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[str(self.name)])


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = HTMLField()
    slug = models.SlugField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    contributor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[str(self.slug)])

    def random_slug(self):
        return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(6)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + '-' + self.random_slug())
        super(Article, self).save(*args, **kwargs)

    def get_delete_url(self):
        return reverse('delete_article', args=[str(self.slug)])

    def get_update_url(self):
        return reverse('update_article', args=[str(self.slug)])
