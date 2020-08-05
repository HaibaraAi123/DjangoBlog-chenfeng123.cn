from django.shortcuts import render
from django.http import HttpResponse
from comment.models import BlogComment
from comment.forms import CommentForm
from .models import Article
import markdown


# Create your views here.
def ArticleDetail(request, id):
    '''
    博客文章详情页面处理函数
    url /myblog/id.html
    '''
    article = Article.objects.get(id=id)
    if article.user != request.user:
        article.views += 1
        article.save(update_fields=['views'])
    # 使用markdown语法 以及代码高亮扩展
    extension_configs = {
        'markdown.extensions.codehilite':{
            #'linenums': 'True'
        }
    }
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ],
        extension_configs=extension_configs)
    article.body = md.convert(article.body)
    # 文章评论模块
    comments = BlogComment.objects.filter(article=id)
    comment_form = CommentForm()
    context = {
        'article': article,
        'toc': md.toc,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'myblog/ArticleDetail.html', context)
