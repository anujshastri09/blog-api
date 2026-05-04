from django.db import models
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

id="like1"
class Post(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    bookmarks = models.ManyToManyField(User, related_name='bookmarked_posts', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Post_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post']  # one like per user per post

    def __str__(self):
        return f"{self.user} liked {self.post}"