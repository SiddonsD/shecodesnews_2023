from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# News Category Model
class Category(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title

# News Story Model
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    category=models.TextChoices(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural='News Stories'

    def __str__(self):
        return self.title
    
# Comments Model
class Comment(models.Model):
    news_story=models.ForeignKey(NewsStory, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment_date_time=models.DateTimeField(auto_now_add=True)
    comment=models.TextField()
    # admin can moderate comments for spam in admin panel by setting status to false
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.comment