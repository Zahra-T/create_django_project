from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import Http404
from .forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def blog_index(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    Post.objects.filter(
        published_date__lte=timezone.now(), status=0).update(status=1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    pages = Paginator(posts, 3)
    page_number = request.GET.get('page')
    # if we use get_page method it internally handel EmptyPage and PageNotAnInteger
    # but if we use page method we should handel those errors by ourselves
    posts = pages.get_page(page_number)
    """try:
        posts = pages.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        raise Http404()
    """
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, id):
    # post = get_object_or_404(Post, pk=id, status=1)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'We got your comment dude!')
            return HttpResponseRedirect(reverse('myBlog:single', kwargs={'id': id}))
        else:
            messages.error(
                request, 'Sorry! we didn\'t get your comment.')
            return HttpResponseRedirect(reverse('myBlog:single', kwargs={'id': id}))
    else:
        allposts = Post.objects.filter(status=1)
        post = get_object_or_404(allposts, pk=id)
        next = allposts.filter(published_date__gt=post.published_date).order_by(
            'published_date').first()
        prev = allposts.filter(published_date__lt=post.published_date).order_by(
            '-published_date').first()
        post.counted_views += 1
        post.save()
        comments = Comment.objects.filter(post__id=id, approved=True)
        context = {'post': post, 'next': next,
                   'prev': prev, 'comments': comments}
        return render(request, 'blog/blog-single.html', context)


# this is an other way that i thought maybe is a better solution. but in this way current view
# will consider in next request. or we can add 1 to the counted_views in blog-single.html.
"""
def single_decorator(func):
    def inner(request, id):
        responce=func(request, id)
        if responce.status_code==200:
            post=Post.objects.get(id=id)
            post.counted_views+=1
            post.save()
        return responce
    return inner

@single_decorator
def blog_single(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)"""


def test_view(request):
    return render(request, 'test.html')


def blog_cat_index(request, cat):
    posts = Post.objects.filter(status=1)
    catposts = posts.filter(category__name=cat)
    context = {'posts': catposts}
    return render(request, 'blog/blog-home.html', context)


def search_view(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if param := request.GET.get('q'):
            posts = posts.filter(Q(title__contains=param)
                                 | Q(content__contains=param))
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
