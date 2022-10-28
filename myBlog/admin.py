from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin
"""@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass"""

class PostAdmin(SummernoteModelAdmin):
    summernote_fields=('content',)
    date_hierarchy= 'create_at'
    list_display=['title','author', 'status','counted_views', 'published_date']
    empty_value_display='-empty-'
    list_filter=('status','author')
    # ro be jeloo - gadim be samte jadid
    ordering=['create_at']
    # ro be aghab - jadid be samte gadim
    ordering=['-create_at']
    # che field haiee dar search dar nazar grefte shavad.
    search_fields=['title','content']
    # fields=('title','content')
    # exclude = ('published_date',)

# admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy= 'created_date'
    list_display=['name', 'subject', 'approved']
    empty_value_display='-empty-'    
    list_filter=('post','approved')
    ordering=['-created_date']
    search_fields=['name','subject', 'message']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
