from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from myblog.models import Article
from .forms import CommentForm
from .models import BlogComment


# Create your views here.
@login_required(login_url='/userprofile/login')
def post_comment(request, article_id, parent_comment_id=None):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.author = request.user

            # 二级回复
            if parent_comment_id:
                parent_comment = BlogComment.object.get(id=parent_comment_id)
                new_comment.parent_id = parent_comment.get_root().id
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                return HttpResponse('200')

            new_comment.save()
            return redirect("myblog:detail", id=article_id)
        else:
            return HttpResponse("error!")
    elif request.method == 'GET':
        comment_form = CommentForm()
        context = {
            'comment_form': comment_form,
            'article_id': article_id,
            'parent_comment_id': parent_comment_id,
        }
        return render(request, 'comment/reply.html', context)
    else:
        return HttpResponse("Error! Only get or post!")