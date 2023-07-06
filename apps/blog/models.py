from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(Base):
    author = models.CharField(max_length=221, null=True, blank=True)
    title = models.CharField(max_length=221)
    slug = models.SlugField(unique_for_date='created_date')
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='blogs/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    @property
    def url_detail_blog(self):
        url = reverse('blog:blog_detail', kwargs={
            'year': self.created_date.year,
            'month': self.created_date.month,
            'day': self.created_date.day,
            'slug': self.slug
        })
        return url


class Comment_blog(Base):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=221)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='blogs/comment/')
    message = models.TextField()

    def __str__(self):
        return f"{self.blog.title}'s comment({self.id})"

    @property
    def children(self):
        child = Comment_blog.objects.filter(top_level_comment_id=self.top_level_comment_id).exclude(
            id=self.top_level_comment_id)
        return child


def comment_post_save(instance, sender, created, *args, **kwargs):
    if created:
        parent = instance
        while parent.parent_comment:
            parent = parent.parent_comment
        instance.top_level_comment_id = parent.id
        instance.save()
    return instance


post_save.connect(comment_post_save, sender=Comment_blog)


def blog_pre_save(instance, sender, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

    return instance


pre_save.connect(blog_pre_save, sender=Blog)
