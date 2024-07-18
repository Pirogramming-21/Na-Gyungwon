from django.shortcuts import render, redirect, get_object_or_404
from .models import Tool
from .forms import ToolForm


def index(req):
    tools = Tool.objects.all()
    ctx = {"tools": tools}
    return render(req, "devtools/tool_list.html", ctx)


def tool_list(req):
    tools = Tool.objects.all()
    ctx = {"tools": tools}
    return render(req, "devtools/tool_list.html", ctx)


def tool_create(req):
    if req.method == "GET":
        form = ToolForm()
        ctx = {"form": form}
        return render(req, "devtools/tool_create.html", ctx)

    form = ToolForm(req.POST, req.FILES)
    if form.is_valid():
        form.save()
    return redirect("devtools:tool_list")


def tool_detail(req, pk):
    tool = Tool.objects.get(id=pk)
    ctx = {"tool": tool, "pk": pk}
    return render(req, "devtools/tool_detail.html", ctx)


def tool_delete(req, pk):
    tool = get_object_or_404(Tool, pk=pk)
    tool.delete()
    return redirect("devtools:tool_list")


def tool_update(req, pk):
    tool = Tool.objects.get(id=pk)
    if req.method == "GET":
        form = ToolForm(instance=tool)
        ctx = {"form": form, "tool": tool, "pk": pk}
        return render(req, "devtools/tool_update.html", ctx)

    form = ToolForm(req.POST, req.FILES, instance=tool)
    if form.is_valid():
        form.save()
    return redirect("devtools:tool_detail", pk)
