# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from myblog.views import Article
from myblog.models import AlbumPhoto
from comment.models import BlogComment


def index_views(request):
    search = request.GET.get('search')
    # 导航栏搜索 文章
    if search:
        Articles = Article.objects.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
            )
    else:
        # search = ''
        Articles = Article.objects.order_by('-created_time')
    comments = BlogComment.objects.order_by('-created_time')
    context = {
            'Articles': Articles,
            'search': search,
            'comments': comments,
    }
    return render(request, 'index.html', context)


def album_views(request):
    '''
    博客导航栏 item-照片墙
    '''
    album = AlbumPhoto.objects.all()
    # 将相册均分成三列
    tmp = int(len(album)/3)
    albums = []
    albums.append(album[0:tmp])
    if len(album) > 3*tmp:
        albums.append(album[tmp:2*tmp+1])
        albums.append(album[2*tmp+1:])
    else:
        albums.append(album[tmp:2*tmp])
        albums.append(album[2*tmp:])
    context = {
        'albums': albums,
    }
    return render(request, 'myblog/album.html', context)


def about_views(request):
    '''
    博客导航栏 item-关于博主
    '''
    context = {

    }
    return render(request, 'myblog/about.html', context)


def onbug_views(request):
    '''
    博客导航栏 item-bug吐槽
    使用留言板功能
    '''
    context = {

    }
    return render(request, 'myblog/onbug.html', context)
