from django.contrib import admin
from .models import Article, Banner, Category, Tag, Rank, FriendLink, AlbumPhoto


# Register your models here.
@admin.register(Article)
class ActicleAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'category', 'views', 'modified_time')
	list_per_page = 50
	ordering = ('-created_time',)
	list_display_links = ('id', 'title')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
	list_display = ('id', 'text_info', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

admin.site.register(Rank)

admin.site.register(FriendLink)
admin.site.register(AlbumPhoto)
