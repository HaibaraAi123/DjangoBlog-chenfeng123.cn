from django.db import models
from django.contrib.auth.models import User


# 文章 分类 Category
class Category(models.Model):
    name = models.CharField('博客分类', max_length=30)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章标签 Tag
class Tag(models.Model):
    name = models.CharField('文章标签', max_length=30)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章 推荐位序
class Rank(models.Model):
    name = models.CharField('文章推荐位序', max_length=100)

    class Meta:
        verbose_name = '推荐位序'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章内容 Article
class Article(models.Model):
    title = models.CharField('标题', max_length=30)
    excerpt = models.TextField('摘要', max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d', verbose_name='文章图片', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    views = models.PositiveIntegerField('阅读量', default=0)
    rank = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, verbose_name='推荐位序', blank=True, null=True)

    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    body = models.TextField()
    '''
    body = UEditorField('内容', width=800, height=500,
                                         toolbars="full", imagePath="upimg/", filePath="upfile/",
                                          upload_settings={"imageMaxSize": 120400},
                                          settings={}, command=None, blank=True)
    '''
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# banner
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


# friend link
class FriendLink(models.Model):
    name = models.CharField('链接名称', max_length=20)
    link_url = models.URLField('网址', max_length=100)

    class Meta:
        """docstring for META"""
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 照片模型
class AlbumPhoto(models.Model):
    '''
    网站主页照片墙中照片模型
    存储照片url title describle
    '''
    photo_title = models.CharField('标题', max_length=50, default='', blank=True)
    photo_url = models.CharField('照片路径', max_length=100)
    photo_describle = models.CharField('内容', max_length=100, default='', blank=True)

    class Meta:
        verbose_name = '照片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.photo_title
