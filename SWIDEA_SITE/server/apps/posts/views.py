from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.http import JsonResponse


# Create your views here.
# urlpatterns = [
#     path("", main, name="main"),
#     path("create/", create, name="create"),
#     path("detail/<int:pk>/", detail, name="detail"),
#     path("delete/<int:pk>/", delete, name="delete"),
#     path("update/<int:pk>/", update, name="update"),
# ]
def index(req):
    posts = Post.objects.all()
    ctx = {"posts": posts}
    return render(req, "posts/list.html", ctx)


def list(req):
    posts = Post.objects.all()
    ctx = {"posts": posts}
    return render(req, "posts/list.html", ctx)


def create(req):
    if req.method == "GET":
        form = PostForm()
        ctx = {"form": form}
        return render(req, "posts/create.html", ctx)

    form = PostForm(req.POST, req.FILES)
    if form.is_valid():
        form.save()
    ctx = {"form": form}
    return redirect("posts:index")


def detail(req, pk):
    post = Post.objects.get(id=pk)
    ctx = {"post": post, "pk": pk}
    return render(req, "posts/detail.html", ctx)


def delete(req, pk):
    Post.objects.get(id=pk).delete()
    return redirect("posts:index")


def update(req, pk):
    post = Post.objects.get(id=pk)
    if req.method == "GET":
        form = PostForm(instance=post)
        ctx = {"form": form, "pk": pk}
        return render(req, "posts/update.html", ctx)

    form = PostForm(req.POST, req.FILES, instance=post)
    if form.is_valid():
        form.save()
    return redirect("posts:detail", pk)


def order(req, order_by=None):
    if order_by == "interest":
        posts = Post.objects.all().order_by("-interest")
    elif order_by == "title":
        posts = Post.objects.all().order_by("title")
    elif order_by == "created":
        posts = Post.objects.all().order_by("created_date")
    elif order_by == "latest":
        posts = Post.objects.all().order_by("-created_date")
    else:
        posts = Post.objects.all()

    ctx = {
        "posts": posts,
        "selected_order_by": order_by,
    }
    return render(req, "posts/list.html", ctx)


def mark(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.marked = not post.marked  # 현재 상태의 반대로 토글
        post.save()
        return JsonResponse({"success": True, "marked": post.marked})

    return JsonResponse({"success": False, "error": "Invalid request method"})


def update_interest(request, pk):
    action = request.POST.get("action")
    post = get_object_or_404(Post, pk=pk)

    if action == "increase":
        post.interest += 1
    elif action == "decrease":
        post.interest -= 1

    post.save()

    return redirect("posts:list")
