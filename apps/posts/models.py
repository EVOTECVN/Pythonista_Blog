from django.db import models
from utils.models import BaseModel
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Category(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='categories')
    description = RichTextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'


class Tag(BaseModel):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="tags")
    description = RichTextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        verbose_name_plural = 'Tags'


class PostModelManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Post(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posts')
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(unique=True)
    published = PostModelManger()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        verbose_name_plural = 'Posts'
