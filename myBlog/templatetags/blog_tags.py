from django import template
from myBlog.models import Category, Post, Comment
register=template.Library()
@register.simple_tag
def function(a):
    return a*a

@register.simple_tag()
def postsnum():
    return Post.objects.filter(status=1).count()

@register.simple_tag(name='posts')
def getposts():
    return Post.objects.filter(status=1)

@register.inclusion_tag('blog/blog-popular-posts.html')
def popularposts():
    posts=Post.objects.filter(status=1).order_by('-counted_views')[:3]
    context={'posts':posts}
    return context

@register.inclusion_tag('blog/blog-categories.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    cats=Category.objects.all()
    cat_dict={}
    for cat in cats:
        cat_dict[cat]=posts.filter(category=cat).count()
    return {'categories':cat_dict}

@register.simple_tag
def latestposts():
    return Post.objects.filter(status=1).order_by('-published_date')[:6]

@register.simple_tag
def comment_number(id):
    return Comment.objects.filter(post__id=id, approved=1).count()
    
