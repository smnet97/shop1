from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('first name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last name'))
    image = models.ImageField(upload_to='authors/')

    @property
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_fullname

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class TagsModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class BlogModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    body = RichTextField(verbose_name=_('body'))
    main_image = models.ImageField(upload_to='blogs/', verbose_name=_('main image'))
    banner_image = models.ImageField(upload_to='blogs/', verbose_name=_('banner image'))
    tags = models.ManyToManyField(TagsModel, verbose_name=_('tag'), related_name='blogs')
    author = models.ForeignKey(AuthorModel, on_delete=models.RESTRICT, verbose_name=_('author'), related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')


class CommentsModel(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    comment = models.TextField(verbose_name=_('comment'))
    blog = models.ForeignKey(BlogModel, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
