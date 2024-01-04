from django.contrib import admin
from .models import Category, NewsStory, Comment


admin.site.register(Category)

class AdminNewsStories(admin.ModelAdmin):
    list_display=('title', 'category', 'pub_date')

admin.site.register(NewsStory, AdminNewsStories)

class AdminComment(admin.ModelAdmin):
    list_display=('news_story', 'comment_date_time', 'comment', 'status')

admin.site.register(Comment, AdminComment)