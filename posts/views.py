from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated
id="like4"
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from drf_spectacular.utils import extend_schema

# 📌 List + Create
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @extend_schema(tags=["Posts"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=["Posts"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# 📌 Retrieve + Update + Delete
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=["Posts"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=["Posts"])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(tags=["Posts"])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class PostListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are authenticated"})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(parent=None)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'author'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ["status","author"]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'views']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'message': 'Unliked'}, status=status.HTTP_200_OK)
        else:
            post.likes.add(user)
            return Response({'message': 'Liked'}, status=status.HTTP_200_OK)
id="like5"
@action(detail=True, methods=['post'])
def bookmark(self, request, pk=None):
        post = self.get_object()
        user = request.user

        if user in post.bookmarks.all():
            post.bookmarks.remove(user)
            return Response({'message': 'Removed bookmark'}, status=status.HTTP_200_OK)
        else:
            post.bookmarks.add(user)
            return Response({'message': 'Bookmarked'}, status=status.HTTP_200_OK)