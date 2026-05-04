from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import PostListCreateView, PostDetailView


urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls