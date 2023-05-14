from django.urls import path

from posts.views import posts, PostDetailView, PostUpdateView, PostDeleteView, PostCreateView

urlpatterns = [
    path('', posts, name='posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='post'),
    path('update-post/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete-post/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('create-post/', PostCreateView.as_view(), name='create'),
]