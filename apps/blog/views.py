from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Blog, Comment_blog, Tag, Category
from .forms import Comment_blogForm
from django.contrib import messages
from django.core.paginator import Paginator


def blog(request):
    blogs = Blog.objects.order_by('-id')
    tags = Tag.objects.order_by('-id')
    tag = request.GET.get('tag')
    if tag:
        blogs = blogs.filter(tags__title__exact=tag)
    paginator = Paginator(blogs, 1)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    ctx = {
        'blogs': page_obj,
        'tags': tags,
    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, **kwargs):
    blogs = get_object_or_404(Blog, slug=kwargs['slug'], created_date__year=kwargs['year'],
                              created_date__month=kwargs['month'],
                              created_date__day=kwargs['day'], )
    blog_comments = Comment_blog.objects.filter(blog_id=blogs.id, parent_comment=None)[:3]
    all_comment = request.GET.get('all')
    if all_comment and all_comment == "True":
        blog_comments = Comment_blog.objects.filter(blog_id=blogs.id, parent_comment=None)
    parent = request.GET.get('parent')
    form = Comment_blogForm()
    if request.method == 'POST':
        form = Comment_blogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            if parent:
                obj.parent_comment_id = parent
            obj.blog_id = blogs.id
            obj.save()
            messages.success(request, 'Your messages was successfully accepted')
            return redirect(blogs.url_detail_blog)
        else:
            messages.error(request, 'Error!')
    ctx = {
        'blog': blogs,
        'blog_comments': blog_comments,
        'form': form,
    }
    return render(request, 'blog/single-blog.html', ctx)
