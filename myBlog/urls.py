from django.urls import path
from .views import blog_index, blog_single, test_view, search_view
from .feeds import LatestPostsFeed
app_name='myBlog'
urlpatterns = [
    path('',blog_index, name='index'),
    path('<int:id>/',blog_single, name='single'),
    path('test', test_view, name='test'),
    path('category/<str:cat_name>', blog_index, name='category'),
    path('author/<str:author_username>',blog_index, name="author" ),
    path('search',search_view, name='search'),
    path('tag/<str:tag_name>',blog_index, name='tag'),
    path('rss/feed/', LatestPostsFeed()),
]