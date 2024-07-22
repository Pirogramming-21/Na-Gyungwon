from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    ctx = {
        "posts": posts,
    }
    return render(request, "main/post_list.html", ctx)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.like = 0
            post.dislike = 0
            form.save()
            return redirect("main:post_list")
        else:
            ctx = {
                "form": form,
            }
            return render(request, "main/post_new.html", ctx)
    elif request.method == "GET":
        form = PostForm()
        ctx = {
            "form": form,
        }
        return render(request, "main/post_new.html", ctx)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req["id"]
    button_type = req["type"]

    post = Post.objects.get(id=post_id)

    if button_type == "like":
        post.like += 1
    else:
        post.dislike += 1

    post.save()

    return JsonResponse({"id": post_id, "type": button_type})


# https://hoik92.github.io/django/2019/06/20/Create-and-Delete-Comment-Using-Django.html


@csrf_exempt
@require_POST
@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()

        return JsonResponse(
            {"success": True, "comment_id": comment.id, "content": comment.content}
        )
    return JsonResponse({"success": False, "error": "Invalid data"})


@login_required
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
    return redirect("main:post_list")
