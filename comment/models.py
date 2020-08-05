from django.db import models
from django.contrib.auth.models import User
from myblog.models import Article
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class BlogComment(MPTTModel):
    article = models.ForeignKey(Article,
        on_delete=models.CASCADE, related_name='blogcomments')
    author = models.ForeignKey(User,
        on_delete=models.CASCADE, related_name='blogcomments')
    parent = TreeForeignKey('self',
        on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    reply_to = models.ForeignKey(User,
        null=True, blank=True, on_delete=models.CASCADE, related_name='replier')
    body = RichTextField()
    created_time = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['created_time']

    def __str__(self):
        return self.body[:20]
