from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')  
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'parent', 'replies']

    def get_replies(self, obj):
        replies = Comment.objects.filter(parent=obj)
        return CommentSerializer(replies, many=True).data

id="like3"
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  
    likes_count = serializers.SerializerMethodField()
    bookmarks_count = serializers.SerializerMethodField()


    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at','bookmarks_count','likes_count']

    def get_likes_count(self, obj):
        return obj.post_likes.count()

    def get_bookmarks_count(self, obj):
        return obj.bookmarks.count()
    
    def get_is_bookmarked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.bookmarks.filter(id=request.user.id).exists()
        return False